import os
from docx import Document
from docx.shared import Inches
import sqlite3
from docx.enum.section import WD_ORIENTATION
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from itertools import islice


def create_word_document(comments_table):
    doc = Document()

    # Get the list of page images from the folder
    image_folder = './tayseer/Pages/'
    image_files = sorted(os.listdir(image_folder), key=lambda x: int(x.split('.')[0]))

    # Iterate over each page and add the corresponding image, comments, and separator
    for page_number, image_file in enumerate(image_files, start=1):
        # Add even page with image to the left
        if page_number % 2 == 0:
            section = doc.sections[-1] if doc.sections else doc.add_section()
            section.orientation = WD_ORIENTATION.LANDSCAPE
            section.page_width = Inches(11)
            section.page_height = Inches(8.5)

            header = section.header
            header.is_linked_to_previous = False
            header_first_page = header.paragraphs[0]
            header_first_page.text = f'Page {page_number}'
            header_first_page.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT

            doc.add_picture(os.path.join(image_folder, image_file), width=Inches(5))

        # Add page number
        doc.add_paragraph(f'Page {page_number}')

        # Retrieve comments from the table for the current page
        page_comments = comments_table.get(page_number, [])

        # Add comments to the document
        for i, comment in enumerate(page_comments, start=1):
            if comment:  # Add comment only if it's not empty
                cleaned_comment = comment.replace('\n', '. ')
                doc.add_paragraph(f'({i}): {cleaned_comment}')

        # Add separator after each comment
        doc.add_paragraph()

        # Add odd page with image to the right
        if page_number % 2 != 0:
            doc.add_picture(os.path.join(image_folder, image_file), width=Inches(5))
            doc.add_page_break()

    # Save the document
    doc.save('output.docx')


def read_comments_from_database():
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    c.execute("SELECT page_number, comment FROM comments ORDER BY page_number")
    rows = c.fetchall()
    comments_table = {}
    for row in rows:
        page_number, comment = row
        comments_table.setdefault(page_number, []).append(comment)
    conn.close()
    return comments_table


# Read comments from the database
comments_table = read_comments_from_database()

# Create the Word document
create_word_document(comments_table)
