import os
from docx import Document
from docx.shared import Inches, Pt
import sqlite3
from docx.enum.section import WD_ORIENTATION
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT


def create_word_document(comments_table):
    doc = Document()

    # Get the list of page images from the folder
    image_folder = './tayseer/Pages/'
    image_files = sorted(os.listdir(image_folder), key=lambda x: int(x.split('.')[0]))

    # Iterate over each page and add the corresponding image, comments, and separator
    for page_number, image_file in enumerate(image_files, start=1):
        section = doc.sections[-1] if doc.sections else doc.add_section()
        section.orientation = WD_ORIENTATION.PORTRAIT
        section.page_width = Inches(8.5)
        section.page_height = Inches(11)

        # Add image to the page
        paragraph = doc.add_paragraph()
        run = paragraph.add_run()
        run.add_picture(os.path.join(image_folder, image_file), width=Inches(3))

        if page_number % 2 == 0:
            paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
        else:
            paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

        # Retrieve comments from the table for the current page
        page_comments = comments_table.get(page_number, [])

        # Add comments to the document
        for i, comment in enumerate(page_comments, start=1):
            if comment:  # Add comment only if it's not empty
                cleaned_comment = comment.replace('\n\r', ' ـ ')
                cleaned_comment = cleaned_comment.replace('\r', ' ـ ')
                cleaned_comment = cleaned_comment.replace('\n', ' ـ ')
                paragraph = doc.add_paragraph()
                run = paragraph.add_run()
                paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
                run.text = 'م'+str(i)+' - ' + cleaned_comment
                paragraph.paragraph_format.line_spacing = Pt(12)


        # Add separator after each comment
        doc.add_paragraph()
        doc.add_page_break()

    # Set consistent page margins for all sections
    for section in doc.sections:
        section.left_margin = Inches(1.27)
        section.right_margin = Inches(1.27)
        section.top_margin = Inches(1.27)
        section.bottom_margin = Inches(1.27)

    # Save the document
    doc.save('output.docx')


def read_comments_from_database():
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    c.execute("SELECT page_number, comment FROM comments where (comment is not null) and (comment <>'') ORDER BY page_number")
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
