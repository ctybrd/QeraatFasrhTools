import json
import sqlite3
import os
from docx import Document
from docx.shared import RGBColor, Pt
from docx.oxml import OxmlElement, ns

def cmyk_to_rgb(c, m, y, k):
    """Convert CMYK values (0 to 1 range) to RGB values (0 to 255 range)."""
    r = 255 * (1 - c) * (1 - k)
    g = 255 * (1 - m) * (1 - k)
    b = 255 * (1 - y) * (1 - k)
    return int(r), int(g), int(b)

def insert_data(cursor, data, pagenumber, doc):
    """Inserts the JSON data into the SQLite database with hierarchical rows and formats them in a Word document.

    Args:
        cursor: A SQLite cursor object.
        data: The JSON data to insert.
        pagenumber: The page number associated with the data.
        doc: The Word document object to add the content to.
    """
    doc.add_paragraph(f"صفحة: {pagenumber}").bold = True

    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS qeraat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_text TEXT,
            word_order INTEGER,
            pagenumber INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS qeraat_chars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            x REAL,
            y REAL,
            h REAL,
            w REAL,
            size REAL,
            color TEXT,
            unicode TEXT,
            upright BOOLEAN,
            fontname TEXT,
            qeraat_id INTEGER,
            FOREIGN KEY(qeraat_id) REFERENCES qeraat(id)
        )
    ''')

    # Insert data into the main table (qeraat)
    for item in data:
        word_text = item.get('word_text', '')
        word_order = item.get('word_order', 0)

        cursor.execute('''
            INSERT INTO qeraat (word_text, word_order, pagenumber)
            VALUES (?, ?, ?)
        ''', (word_text, word_order, pagenumber))

        # Get the inserted row ID to use as a foreign key
        qeraat_id = cursor.lastrowid

        # Process `detail_title_chars`
        process_detail_chars(cursor, item.get('detail_title_chars', []), qeraat_id, doc)

        # Process `quran_ten_word_mp3`
        for mp3_section in item.get('quran_ten_word_mp3', []):
            process_detail_chars(cursor, mp3_section.get('detail_chars', []), qeraat_id, doc)

def process_detail_chars(cursor, detail_chars, qeraat_id, doc):
    """Processes detail characters and inserts them into the database and Word document."""
    paragraph = doc.add_paragraph()  # Start a new paragraph
    for char_data in detail_chars:
        text = char_data.get('unicode')
        # text=text.replace('﴿','<b>').replace('﴾','</b>')
        # text=text.replace('<b>','﴾').replace('</b>','﴿',)
        text=text.replace(')','<b>').replace('(','</b>')
        text=text.replace('<b>','(').replace('</b>',')',)
        text = 'ـ ' + text

        run = paragraph.add_run(text)

        # Set font name
        fontname = char_data.get('fontname')
        if fontname:
            run.font.name = fontname
            rPr = run._element.get_or_add_rPr()
            rFonts = rPr.get_or_add_rFonts()
            rFonts.set(ns.qn('w:ascii'), fontname)
            rFonts.set(ns.qn('w:hAnsi'), fontname)
            rFonts.set(ns.qn('w:cs'), fontname)

        # Set font color
        color = char_data.get('color')
        if isinstance(color, dict) and 'ncolor' in color:
            cmyk_values = color['ncolor']
            if len(cmyk_values) == 4:
                r, g, b = cmyk_to_rgb(*cmyk_values)
                run.font.color.rgb = RGBColor(r, g, b)

        # Set font size (convert to Pt)
        size = char_data.get('size')
        if size:
            run.font.size = Pt(size)

        # Handle text direction if 'upright' is specified
        if char_data.get('upright'):
            rPr = run._element.get_or_add_rPr()
            rtl = OxmlElement('w:rtl')
            rtl.text = '0'  # '1' for right-to-left, '0' for left-to-right
            rPr.append(rtl)

        # Insert data into qeraat_chars table
        cursor.execute('''
            INSERT INTO qeraat_chars (x, y, h, w, size, color, unicode, upright, fontname, qeraat_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            char_data.get('x', 0), char_data.get('y', 0), char_data.get('h', 0), char_data.get('w', 0),
            size, json.dumps(color), text, char_data.get('upright'), fontname, qeraat_id
        ))

def main():
    """Reads JSON data from multiple files in a folder, inserts it into the database, and commits the changes, also generates a Word document with the formatted text."""
    script_path = os.path.abspath(__file__)
    drive, _ = os.path.splitdrive(script_path)
    drive = drive + '/'
    folder_path = os.path.join(drive, 'Qeraat/QeraatFasrhTools_Data/Ten_Readings/json')
    db_path = os.path.join(drive, 'Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db')
    print(db_path)

    # Establish a connection to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create a new Word document
    doc = Document()

    try:
        # Extract numeric parts of filenames and sort them
        files = sorted(
            [f for f in os.listdir(folder_path) if f.startswith("Qeraat_") and f.endswith(".json")],
            key=lambda x: int(x.split("_")[1].split(".")[0])
        )

        for filename in files:
            pagenumber = int(filename.split("_")[1].split(".")[0])  # Extract pagenumber from filename
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
                insert_data(cursor, data, pagenumber, doc)

                # Insert a page break after processing each file
                doc.add_page_break()

        # Save the Word document
        doc.save('qeraat_Content.docx')

        # Commit all changes to the database
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()  # Rollback changes if an error occurs
    finally:
        cursor.close()  # Close the cursor
        conn.close()  # Close the database connection

if __name__ == '__main__':
    main()
