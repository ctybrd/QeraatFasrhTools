import shutil
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
        try:
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
        except Exception as e:
            print(f"Error processing annotations on page {pageno}: {e}")


    return comments


def create_table_sqlite():
    conn = sqlite3.connect('E:/Qeraat/farsh_v5.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS shmrly
                 (qaree TEXT, page_number INTEGER, color TEXT, type NUMERIC, x REAL, y REAL, width REAL)''')
    conn.commit()
    conn.close()

def insert_comments_sqlite(comments,qaree_key):
    conn = sqlite3.connect('E:/Qeraat/farsh_v5.db')
    c = conn.cursor()
    # Delete rows with value "A" in the field "qaree"
    c.execute("DELETE FROM shmrly WHERE qaree = ?", (qaree_key,))
    c.execute("UPDATE shmrly SET style='S' where style is null")
    for comment in comments:
        print(comment['content'], comment['coordinates'], comment['color'])

        coordinates = str(comment['coordinates'])
        matches = re.findall(r'(\d+\.?\d*)', coordinates)
        x1, y1, x2, y2 = matches

        color_values = get_color_name(str(comment['color']))
        color_type = get_color_type(color_values)

        c.execute("INSERT INTO shmrly(qaree, page_number, color, type, x, y, width,style) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (qaree_key, comment['pageno'], str(color_values), str(color_type), float((float(x1)-81.0)/443.0), 1-(float((float(y1)-81.0)/691.0)),max(0.05, float((float(x2) - float(x1)) / 443.0)),str(comment['style'])))  # Use converted values

    conn.commit()
    conn.close()

def get_color_name(color_values):
    fraction_values = eval(color_values)
    print(color_values)
    rgb_values = tuple(int(round(val * 255 / 128) * 128) for val in fraction_values)
   
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
qaree_key = "A" 
pdf_path = 'e:/Qeraat/Warsh.pdf'
line_comments = extract_line_comments(pdf_path)


# Create the table in SQLite
# create_table_sqlite()

# Insert line comments into SQLite
insert_comments_sqlite(line_comments,qaree_key)

file_path = 'E:/Qeraat/farsh_v5.db'
destination_folders = [
    'E:/Qeraat/Wursha_QuranHolder/other/data/',
    'E:/Qeraat/Wursha_QuranHolder/platforms/android/app/build/intermediates/assets/debug/mergeDebugAssets/www/',
    'E:/Qeraat/Wursha_QuranHolder/platforms/android/app/src/main/assets/www/',
    'E:/Qeraat/Wursha_QuranHolder/www/'
]


for folder in destination_folders:
    destination_file = folder + 'farsh_v4.db'
    shutil.copy(file_path, destination_file)

print("File copied to the specified folders.")
