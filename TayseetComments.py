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
                    x_coordinate REAL,
                    y_coordinate REAL,
                    annotation_type TEXT,
                    comment TEXT,
                    icon TEXT,
                    color TEXT,
                    width INTEGER
                )''')
    conn.commit()
    conn.close()

def insert_comment(conn, page_number, x_coordinate, y_coordinate, annotation_type, comment, icon, color, width):
    c = conn.cursor()
    c.execute('''INSERT INTO comments (page_number, x_coordinate, y_coordinate, annotation_type, comment, icon, color, width)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (page_number, str(x_coordinate), str(y_coordinate), annotation_type, comment, str(icon), str(color), width))

def extract_comments(source_pdf_path):
    create_database()
    conn = sqlite3.connect('comments.db')
    comments = []
    with io.open(source_pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_number, page in enumerate(reader.pages, 1):
            annotations = page['/Annots']
            for annotation in annotations:
                annotation_obj = annotation.get_object()
                x_coordinate = annotation_obj['/Rect'][0]
                y_coordinate = annotation_obj['/Rect'][1]
                annotation_type = annotation_obj['/Subtype']
                comment = annotation_obj.get('/Contents', '')
                if annotation_type == '/Text' and '/Name' in annotation_obj:
                    icon = annotation_obj['/Name']
                else:
                    icon = None
                color = annotation_obj.get('/C', [0, 0, 0])
                width = annotation_obj['/Border'][0] if '/Border' in annotation_obj else None
                insert_comment(conn, page_number, x_coordinate, y_coordinate, annotation_type, comment, icon, color, width)
                comments.append((page_number, comment))
        conn.commit()
    conn.close()
    return comments

# Usage example
source_pdf_path = 'E:/Qeraat/QeraatFasrhTools/Tayseer/shamarly10th.pdf'
comments = extract_comments(source_pdf_path)
