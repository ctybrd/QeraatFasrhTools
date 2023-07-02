import sqlite3
from docx import Document
from docx.shared import Inches
from bs4 import BeautifulSoup
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH
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

        # Check if the page number is even or odd
        if current_page % 2 == 0:
            # Create a new section and set the alignment to left
            section = doc.add_section(WD_SECTION.NEW_PAGE)
            section.left_margin = Inches(1)
            section.right_margin = Inches(2)

            # Add the image with left alignment
            run = doc.add_paragraph().add_run()
            run.add_picture(image_path, width=Inches(3))
        else:
            # Create a new section and set the alignment to right
            section = doc.add_section(WD_SECTION.NEW_PAGE)
            section.left_margin = Inches(2)
            section.right_margin = Inches(1)

            # Add the image to a new paragraph with right alignment
            paragraph = doc.add_paragraph()
            paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            run = paragraph.add_run()
            run.add_picture(image_path, width=Inches(3))

    # Process the HTML text and concatenate it
    soup = BeautifulSoup(text, 'html.parser')
    concatenated_text += soup.get_text() + " "  # Modify the separator as needed

# Add the last page's text to the document
doc.add_paragraph(concatenated_text)

# Save the Word document
doc.save('output.docx')

# Close the database connection
conn.close()
