import io
import PyPDF2
import sqlite3
from reportlab.pdfgen import canvas

def create_database():
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS comments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    page_number INTEGER,
                    x_coordinate NUMERIC,
                    y_coordinate NUMERIC,
                    annotation_type TEXT,
                    comment TEXT,
                    icon TEXT,
                    color TEXT,
                    width TEXT
                )''')
    conn.commit()
    conn.close()

def insert_comment(page_number, x_coordinate, y_coordinate, annotation_type, comment, icon, color, width=None):
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    c.execute('''INSERT INTO comments (page_number, x_coordinate, y_coordinate, annotation_type, comment, icon, color, width)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (page_number, x_coordinate, y_coordinate, annotation_type, comment, icon, str(color), str(width)))
    conn.commit()
    conn.close()

def extract_comments(source_pdf_path):
    create_database()
    comments = []
    with open(source_pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_number, page in enumerate(reader.pages, 1):
            annotations = page['/Annots']
            if annotations:
                for annotation in annotations:
                    annotation_obj = annotation.get_object()
                    x = annotation_obj['/Rect'][0]
                    y = annotation_obj['/Rect'][1]
                    annotation_type = annotation_obj['/Subtype']
                    comment = annotation_obj.get('/Contents', '')
                    if annotation_type == '/Text' and '/Name' in annotation_obj:
                        icon = annotation_obj['/Name']
                    else:
                        icon = None
                    color = annotation_obj.get('/C', [0, 0, 0])  # Default color if /C key is not found
                    width = annotation_obj['/Border'][0] if '/Border' in annotation_obj else None
                    insert_comment(page_number, x, y, annotation_type, comment, icon, color, width)
                    comments.append((page_number, comment))
    return comments

# Usage example
source_pdf_path = 'E:/Qeraat/Tayseer/shamarly10th.pdf'
comments = extract_comments(source_pdf_path)
