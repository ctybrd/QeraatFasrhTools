import sqlite3
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_COLOR_INDEX
from docx.shared import RGBColor

def transliterate_number(number):
    mapping = {
        '0': '٠',
        '1': '١',
        '2': '٢',
        '3': '٣',
        '4': '٤',
        '5': '٥',
        '6': '٦',
        '7': '٧',
        '8': '٨',
        '9': '٩',
        '(': ')',
        ')': '(',
        '[': ']',
        ']': '[',
        '.' : '',                  
    }
    return ''.join(mapping.get(char, char) for char in str(number))

# Connect to the SQLite database
conn = sqlite3.connect("E:/Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db")
cursor = conn.cursor()

# Execute the SQL query
sql_query = """
    SELECT aya, sub_subject, reading, page_number2 
    FROM Asbahani 
    ORDER BY aya_index, id
"""

cursor.execute(sql_query)

# Create a new Word document
doc = Document()

# Set the page width to 32mm
section = doc.sections[0]
section.page_width = Pt(32 * 28.35)  # converting mm to points (1 mm = 28.35 points)

# Iterate through the SQL results and add them to the document
current_page_number = None
for aya, sub_subject, reading, page_number in cursor.fetchall():
    # Add new page for each change in value of page_number2
    if current_page_number is None or current_page_number != page_number:
        doc.add_page_break()
        current_page_number = page_number

    # Add block content to the document
    para = doc.add_paragraph()
    
     # Sub_subject column value in red, bold, and large font
    sub_subject_run= para.add_run(transliterate_number(f"{aya} "))
    sub_subject_run.font.size = Pt(10)
    sub_subject_run = para.add_run(f"{sub_subject}\n")
    sub_subject_run.font.bold = True
    sub_subject_run.font.size = Pt(14)
    sub_subject_run.font.color.rgb = RGBColor(0xFF, 0x00, 0x00)

    # Reading column value in black normal font
    editedtext = reading.replace("ـ", "")
    editedtext =transliterate_number('0'+editedtext) # for arabic direction added arabic 0

    # print(editedtext)
    # print(reading)
    sub_subject_run = para.add_run(editedtext)
    sub_subject_run.font.size = Pt(11)
    sub_subject_run.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

# Save the document to the specified folder
output_folder = "E:/Qeraat/QeraatFasrhTools/QeraatSearch/output"
doc.save(output_folder + "/quran_data.docx")

# Close the database connection
conn.close()
