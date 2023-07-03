import sqlite3
from docx import Document
from docx.shared import Inches
from bs4 import BeautifulSoup
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt

# Connect to the SQLite database
conn = sqlite3.connect('e:/qeraat/data_v15.db')
cursor = conn.cursor()

# Execute the query to retrieve data from both tables
query = '''
SELECT mj.text, ms.page_number
FROM book_jlalin AS mj
JOIN mosshf_shmrly AS ms ON mj.aya_index = ms.aya_index
'''
cursor.execute(query)
data = cursor.fetchall()

# Create a new Word document
doc = Document()

# Set consistent page margins for all sections
for section in doc.sections:
    section.left_margin = Inches(1.27)
    section.right_margin = Inches(1.27)
    section.top_margin = Inches(1.27)
    section.bottom_margin = Inches(1.27)

# Set default font size and justification for the document
for style in doc.styles:
    if style.type == 1:
        paragraph_format = style.paragraph_format
        paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        paragraph_format.space_after = Pt(6)
        paragraph_format.space_before = Pt(6)
        run = style.font
        run.size = Pt(12)

# Initialize variables for tracking current page number and concatenated text
current_page = None
concatenated_text = ""

# Iterate over the retrieved data
for text, page_number in data:
    # Check if the page has changed
    if current_page is None or current_page != page_number:
        # Add the concatenated text and image to the document (except for the first iteration)
        if current_page is not None:
            # Add a new paragraph with the concatenated text
            doc.add_paragraph(concatenated_text)

            # Add a page break
            doc.add_page_break()

        # Update the current page number and reset the concatenated text
        current_page = page_number
        concatenated_text = ""

        # Add the image to the page
        image_path = f'E:/Qeraat/pages/{current_page}.jpg'  # Replace with the actual path to the folder and image file extension

        # Add the image to a new paragraph with left or right alignment based on page number
        paragraph = doc.add_paragraph()
        run = paragraph.add_run()
        run.add_picture(image_path, width=Inches(3))

        if current_page % 2 == 0:
            paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
        else:
            paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

    # Process the HTML text and concatenate it
    soup = BeautifulSoup(text, 'html.parser')
    concatenated_text += soup.get_text() + " "  # Modify the separator as needed

# Add the last page's text to the document
doc.add_paragraph(concatenated_text)

# Save the Word document
doc.save('output.docx')

# Close the database connection
conn.close()
