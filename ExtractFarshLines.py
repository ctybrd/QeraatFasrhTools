import pyodbc
import sqlite3
import re
from PyPDF2 import PdfReader

import matplotlib.colors as mcolors
import webcolors

def extract_line_comments(pdf_path):
    comments = []
    pdf = PdfReader(pdf_path)

    for pageno, page in enumerate(pdf.pages):
        #for test
        #if pageno >= 7:
        #     break  # Exit the loop after processing the 7th page
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
                        'pageno': pageno+1,
                        'coordinates': annotation.get_object()['/Rect'],
                        'color': annotation.get_object()['/C']
                    }
                    comment['style'] = 'S'
                    if '/BS' in annotation.get_object():
                        if '/S' in annotation.get_object()['/BS']:
                            comment['style'] = str(annotation.get_object()['/BS']['/S'])
                    if comment['style']=='/D':
                        comment['style'] = 'D'
                    comments.append(comment)
                    print(comment)

    return comments


def create_table_sqlite():
    conn = sqlite3.connect('E:/Qeraat/farsh_v5.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS shmrly
                 (qaree TEXT, page_number INTEGER, color TEXT, type NUMERIC, x REAL, y REAL, width REAL)''')
    conn.commit()
    conn.close()


def create_table_sql_server(connection):
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Farsh_Lines
                     (qaree VARCHAR(50), page_number INT, color VARCHAR(50), type VARCHAR(50), x FLOAT, y FLOAT, width FLOAT)''')
    connection.commit()


def insert_comments_sqlite(comments):
    conn = sqlite3.connect('E:/Qeraat/farsh_v5.db')
    c = conn.cursor()
    # Delete rows with value "WA" in the field "qaree"
    c.execute("DELETE FROM shmrly WHERE qaree = ?", ("A",))

    for comment in comments:
        print(comment['content'], comment['coordinates'], comment['color'])

        coordinates = str(comment['coordinates'])
        matches = re.findall(r'(\d+\.?\d*)', coordinates)
        x1, y1, x2, y2 = matches

        color_values = get_color_name(str(comment['color']))
        color_type = get_color_type(color_values)

        c.execute("INSERT INTO shmrly(qaree, page_number, color, type, x, y, width,style) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  ("A", comment['pageno'], str(color_values), str(color_type), float((float(x1)-81.0)/443.0), 1-(float((float(y1)-81.0)/691.0)),float((float(x2) - float(x1))/443.0),str(comment['style'])))  # Use converted values

    conn.commit()
    conn.close()


def insert_comments_sql_server(connection, comments):
    cursor = connection.cursor()
    # Delete rows with value "WA" in the field "qaree"
    cursor.execute("DELETE FROM Farsh_Lines WHERE qaree = ?", ("WA",))

    for comment in comments:
        print(comment['content'], comment['coordinates'], comment['color'])

        coordinates = str(comment['coordinates'])
        matches = re.findall(r'(\d+\.?\d*)', coordinates)
        x1, y1, x2, y2 = matches

        color_values = get_color_name(str(comment['color']))
        color_type = get_color_type(color_values)

        cursor.execute("INSERT INTO Farsh_Lines(qaree, page_number, color, type, x, y, width,style) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       ("WA", comment['pageno'], str(color_values), str(color_type), float(x1), float(y1), float(x2) - float(x1),str(comment['style'])))  # Use converted values

    connection.commit()



def get_color_name(color_values):
    fraction_values = eval(color_values)
    print(color_values)
    rgb_values = tuple(int(round(val * 255 / 128) * 128) for val in fraction_values)
    # if rgb_values == (204, 153, 0):
    #     rgb_values = (128, 128, 0)
    
    try:
         color_name = webcolors.rgb_to_name(rgb_values)
    except ValueError:
    # Handle the case of an unknown color
        color_name = 'black'
    if (color_name == "lime"):
        color_name = "green"
    return color_name



def get_color_type(color_values):
    if color_values == "red":
        return "Farsh"
    elif (color_values == "green") or (color_values == "lime") :
        return "Ebdal"
    elif color_values == "cyan":
        return "Sound"
    elif color_values == "blue":
        return "Naql"
    elif (color_values == "magenta") or (color_values == "purple"):
        return "Badal+Leen"
    elif (color_values == "yellow") or (color_values == "olive"):
        return "MeemSela"

    
    else:
        return "Farsh"


# Extract line comments from the PDF
pdf_path = 'e:/Qeraat/Warsh.pdf'
line_comments = extract_line_comments(pdf_path)

# Establish a connection to the SQL Server database
# sql_server_connection = pyodbc.connect('Driver={SQL Server};Server=localhost;Database=Shmrly;Trusted_Connection=yes;')

# Create the table in SQLite
# create_table_sqlite()

# Create the table in SQL Server
# create_table_sql_server(sql_server_connection)

# Insert line comments into SQLite
insert_comments_sqlite(line_comments)

# Insert line comments into SQL Server
# insert_comments_sql_server(sql_server_connection, line_comments)

# Close the SQL Server connection
# sql_server_connection.close()

# update Farsh_Lines set bakX=x,baky=y,bakwidth=width where qaree='WA'

# update Farsh_Lines set x=(bakX-79)/443 where qaree='WA'
# update Farsh_Lines set y= 1-(baky-81)/691 where qaree='WA'
# update Farsh_Lines set width=(bakwidth)/443 where qaree='WA'