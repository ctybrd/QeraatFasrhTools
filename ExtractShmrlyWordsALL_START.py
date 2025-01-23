import os
import sqlite3
import re
from PyPDF2 import PdfReader

def extract_line_comments(pdf_path):
    comments = []
    pdf = PdfReader(pdf_path)
    for pageno, page in enumerate(pdf.pages):
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
                            'pageno': pageno + 1,
                            'coordinates': annotation.get_object()['/Rect'],
                            'color': annotation.get_object()['/C']
                        }
                        if '/NM' in annotation.get_object():
                            linename = str(annotation.get_object()['/NM']).strip('()')
                            parts = linename.split('-')
                            if len(parts) >= 2:
                                comment['wordindex'] = parts[0]
                                comment['wordsno'] = parts[1]
                        if annotation.get_object()['/C']:
                            color = annotation.get_object()['/C']
                            if color != [1, 0, 0] and color != [0, 0, 1]:
                                comment['clc'] = 2
                        if '/BS' in annotation.get_object():
                            if '/S' in annotation.get_object()['/BS']:
                                comment['style'] = str(annotation.get_object()['/BS']['/S'])
                        if comment.get('style') == '/D':
                            comment['style'] = 'D'
                        if '/LE' in annotation.get_object():
                            le_value = str(annotation.get_object()['/LE'])
                            if le_value == "['/Circle', '/None']":
                                comment['circle'] = '2'
                            elif le_value == "['/None', '/Circle']":
                                comment['circle'] = '1'
                        print(f"Processing page {pageno}, wordindex {str(comment['wordindex'])} -  {str(comment['wordsno'])}")  
                        comments.append(comment)
        except Exception as e:
            print(f"Error processing annotations on page {pageno}: {e}")
            pass
    return comments

def update_words_xyw(comments):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    xshift = 81.0
   
    for comment in comments:
        try:
            coordinates = str(comment['coordinates'])
            matches = re.findall(r'(\d+\.?\d*)', coordinates)
            if len(matches) == 4:
                x1, y1, x2, y2 = map(float, matches)
                wordindex = comment.get('wordindex')
                wordsno = comment.get('wordsno')
                print(f"Updating page {str(comment['pageno'])} word {str(comment['wordindex'])} - {str(comment['wordsno'])}")  
                if wordindex and wordsno:
                    c.execute(
                        "UPDATE wordsall SET x = ?, y = ?, width = ?, clc = 2 WHERE wordindex = ? AND wordsno = ?",
                        (
                            (float(x1) - xshift) / 443.0,  # Normalize x
                            1 - (float((float(y1) - 81.0) / 691.0)),  # Normalize y
                            (x2 - x1) / 443.0,  # Calculate width
                            wordindex,
                            wordsno
                        )
                    )
        except Exception as e:
            print(f"Error processing annotations on page {comment['wordindex']}: {e}")
            pass

    conn.commit()
    conn.close()

def adjust_line_positions():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Retrieve all rows with clc = 2, ordered by page_number2, lineno2, and wordindex
    c.execute("SELECT wordindex, wordsno, x, width, clc, lineno2 FROM wordsall WHERE clc = 2 ORDER BY page_number2,lineno2, x")
    rows = c.fetchall()

    if not rows:
        print("No rows found with clc = 2.")
        conn.close()
        return

    margin = 0.005  # Define the margin
    current_lineno2 = None
    line_rows = []

    def process_line_rows(line_rows):
        for i, row in enumerate(line_rows):
            wordindex, wordsno, x, width, clc, lineno2 = row

            if i < len(line_rows) - 1:
                next_x = line_rows[i + 1][2]  # x of the next row
                new_width = abs(next_x - x) - margin
            else:
                new_width = 0.98 - x  # Last row

            c.execute(
                "UPDATE wordsall SET width = ? WHERE wordindex = ? AND wordsno = ?",
                (new_width, wordindex, wordsno)
            )
            print(f"Updated wordindex {wordindex}, wordsno {wordsno}, lineno2 {lineno2}: width = {new_width}")

    for row in rows:
        _, _, _, _, _, lineno2 = row
        if current_lineno2 is None:
            current_lineno2 = lineno2

        if lineno2 != current_lineno2:
            process_line_rows(line_rows)
            current_lineno2 = lineno2
            line_rows = []

        line_rows.append(row)

    if line_rows:
        process_line_rows(line_rows)

    sqly = """
        WITH MaxValues AS (
            SELECT 
                page_number2, 
                lineno2, 
                MAX(y) AS max_y
            FROM wordsall
            GROUP BY page_number2, lineno2
        )
        UPDATE wordsall 
        SET y = (
            SELECT max_y 
            FROM MaxValues mv
            WHERE mv.page_number2 = wordsall.page_number2 AND mv.lineno2 = wordsall.lineno2
        )
        WHERE clc = 2;
    """
    c.execute(sqly)
    conn.commit()
    conn.close()
    print("Adjustment process completed.")

run_adjustment_only = False
script_path = os.path.abspath(__file__)
drive, _ = os.path.splitdrive(script_path) 
drive = drive + '/'
db_path = os.path.join(drive, 'Qeraat', 'QeraatFasrhTools', 'QeraatSearch', 'qeraat_data_simple.db')

if __name__ == '__main__':
    if not run_adjustment_only:
        qaree_file = os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'Musshaf', 'ShmrlyWords_start.pdf')

        if os.path.exists(qaree_file):
            comments = extract_line_comments(qaree_file)
            update_words_xyw(comments)
            print("Line comments extracted and inserted from", qaree_file)
        else:
            print("File not found:", qaree_file)
    adjust_line_positions()
