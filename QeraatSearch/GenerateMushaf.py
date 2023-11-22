import sqlite3
from docx import Document
from docx.shared import RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Inches

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
        '(':' ',
        ')': ' ',
    }
    return ''.join(mapping.get(char, char) for char in str(number))

# Connect to the SQLite database
conn = sqlite3.connect('E:/Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db')
cursor = conn.cursor()

# Execute the SQL query
query = """
    SELECT page_number2,
    aya, sub_subject || 
    CASE 
        WHEN count_words = 1 THEN '' 
        WHEN count_words = 2 THEN ' (معا)' 
        ELSE ' (جميعا)' 
    END as sub_subject, 
    CASE 
        WHEN q6 IS NOT NULL THEN '' 
        ELSE 
            CASE 
                WHEN r6_1 IS NOT NULL THEN 'خلف ' 
                ELSE 'خلاد ' 
            END 
    END as subqaree,
    sub_subject, ifnull(readingresult,'') readingresult , reading 
    FROM quran_data 
    WHERE qareesrest LIKE '%حمزة%' and IFNULL(r5_2, 0) = 0 
    ORDER BY page_number2, aya, id;
"""

cursor.execute(query)
rows = cursor.fetchall()

# Close the database connection
conn.close()

# Create a new Word document
doc = Document()

# Iterate through the results and add content to the Word document
for i, row in enumerate(rows):
    page_number2, aya, sub_subject, subqaree, sub_subject, readingresult, reading = row

    # Add a page break after each page_number2 change, except for the first page
    if i != 0 and rows[i - 1][0] != page_number2:
        doc.add_page_break()

        # Add the image to the Word document (replace 'image_path' with the actual path to your images)
        paragraph = doc.add_paragraph()
        run = paragraph.add_run()
        image_path = f'e:/pageshamza/{page_number2}.png'
        run.add_picture(image_path, width=Inches(4))

    # Add the text to the Word document with different colors for each field
    paragraph = doc.add_paragraph()
    run = paragraph.add_run()
    formatted_aya = transliterate_number(aya)
    run.add_text(f"{formatted_aya} ـ ")
    run.font.color.rgb = RGBColor(0, 0, 0)  

    run = paragraph.add_run(f"{sub_subject} : ")
    run.font.color.rgb = RGBColor(255, 0, 0)  

    run = paragraph.add_run(f"{readingresult} ")
    run.font.color.rgb = RGBColor(0, 128, 128)  
    readingclean = reading.replace(')',' ').replace('(',' ')

    run = paragraph.add_run(f"{subqaree} {readingclean}")
    run.font.color.rgb = RGBColor(0, 0, 0) 

# Save the Word document
doc.save('e:/pageshamza/Combined_Document.docx')
