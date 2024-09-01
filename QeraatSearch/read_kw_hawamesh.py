import json
import sqlite3
import os
from docx import Document
from docx.shared import RGBColor, Pt
from docx.oxml import OxmlElement, ns
from bidi.algorithm import get_display
import arabic_reshaper

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

    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Hawamesh (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modified TEXT,
            order1 INTEGER,
            pagenumber INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Hawamesh_chars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            x0 REAL,
            x1 REAL,
            y0 REAL,
            y1 REAL,
            line INTEGER,
            size REAL,
            color TEXT,
            add_tab BOOLEAN,
            text_y0 REAL,
            text_y1 REAL,
            unicode TEXT,
            upright BOOLEAN,
            fontname TEXT,
            is_new_line BOOLEAN,
            add_single_space BOOLEAN,
            Hawamesh_id INTEGER,
            FOREIGN KEY(Hawamesh_id) REFERENCES Hawamesh(id)
        )
    ''')

    # Insert data into the main table (Hawamesh)
    for item in data:
        cursor.execute('''
            INSERT INTO Hawamesh (modified, order1, pagenumber)
            VALUES (?, ?, ?)
        ''', (item['modified'], item['order'], pagenumber))

        # Get the inserted row ID to use as a foreign key
        Hawamesh_id = cursor.lastrowid

        # Insert data into the child table (hawamesh_chars)
        paragraph = doc.add_paragraph()  # Start a new paragraph
        for char_data in item.get('hawamesh_chars', []):
            text = char_data.get('unicode')

            if text == "*" or text[0] == '-':  # Break before '*'
                paragraph = doc.add_paragraph()  # Start a new paragraph
            
            # reshaped_text = arabic_reshaper.reshape(text)
            # bidi_text = get_display(reshaped_text)
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

def main():
    """Reads JSON data from multiple files in a folder, inserts it into the database, and commits the changes, also generates a Word document with the formatted text."""
    script_path = os.path.abspath(__file__)
    drive, _ = os.path.splitdrive(script_path) 
    drive = drive + '/'
    folder_path = os.path.join(drive, 'Qeraat/QeraatFasrhTools_Data/Ten_Readings/json')
    db_path = os.path.join(drive, 'Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db')
    print (db_path)
    # Establish a connection to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create a new Word document
    doc = Document()

    try:
        for filename in os.listdir(folder_path):
            if filename.startswith("Hawamesh_") and filename.endswith(".json"):
                pagenumber = int(filename.split("_")[1].split(".")[0])  # Extract pagenumber from filename
                with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    insert_data(cursor, data, pagenumber, doc)
                
                # Insert a page break after processing each file
                doc.add_page_break()

        # Save the Word document
        doc.save('Hawamesh_Content.docx')

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
