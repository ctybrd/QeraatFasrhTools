import sqlite3
import re
from PyPDF2 import PdfReader

def extract_line_comments(pdf_path):
    comments = []
    pdf = PdfReader(pdf_path)

    for pageno, page in enumerate(pdf.pages):
        annotations = page['/Annots']
        if annotations:
            for annotation in annotations:
                if isinstance(annotation, str):
                    annotation = pdf.get_object(annotation)
                elif isinstance(annotation, dict):
                    annotation = pdf._buildIndirectObject(annotation)

                if annotation.get_object()['/Subtype'] == '/Line':
                    comment = {
                        'content': ' ',
                        'pageno': pageno,
                        'coordinates': annotation.get_object()['/Rect'],
                        'color': annotation.get_object()['/C']
                    }
                    comment['style'] = 'SOLID'
                    if '/BS' in annotation.get_object():
                        if '/S' in annotation.get_object()['/BS']:
                            comment['style'] = str(annotation.get_object()['/BS']['/S'])
                    comments.append(comment)
                    print(comment)

    return comments


def create_table():
    conn = sqlite3.connect('e:/comments.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS comments
                 (page INTEGER, comment TEXT, x1 REAL, y1 REAL, x2 REAL, y2 REAL, coordinates TEXT, color TEXT, color_name TEXT, style TEXT)''')
    conn.commit()
    conn.close()


def insert_comments(comments):
    conn = sqlite3.connect('e:/comments.db')
    c = conn.cursor()

    for comment in comments:
        print(comment['content'], comment['coordinates'], comment['color'])

        coordinates = str(comment['coordinates'])
        matches = re.findall(r'(\d+\.?\d*)', coordinates)
        x1, y1, x2, y2 = matches

        color_values = comment['color']
        color_name = get_color_name(str(color_values))
        
        c.execute("INSERT INTO comments VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (comment['pageno'], str(comment['content']), float(x1), float(y1), float(x2), float(y2),
                   str(coordinates), str(color_values), str(color_name), str(comment['style'])))

    conn.commit()
    conn.close()


def get_color_name(color_values):
    distinct_colors = {
        '[1, 0, 0]': 'Red',
        '[0, 1, 0]': 'Green',
        '[0, 1, 1]': 'Cyan',
        '[0, 0, 1]': 'Blue',
        '[1, 0, 1]': 'Magenta',
        '[0.745, 0.745, 0]': 'Yellow'
    }
    
    for color, name in distinct_colors.items():
        if color == color_values:
            return name

    return 'Unknown'


# Extract line comments from the PDF
pdf_path = 'e:/Warsh.pdf'
line_comments = extract_line_comments(pdf_path)

# Create SQLite table
create_table()

# Insert line comments into the SQLite table
insert_comments(line_comments)
