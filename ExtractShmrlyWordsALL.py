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
                            # Extract wordindex and wordsno from linename
                            # Name pattern: /NM (wordindex-wordsno-surah-ayah)
                            linename = str(annotation.get_object()['/NM']).strip('()')  # Remove brackets
                            parts = linename.split('-')
                            if len(parts) >= 2:
                                comment['wordindex'] = parts[0]  # First part before the dash
                                comment['wordsno'] = parts[1]   # Second part after the first dash
                        if annotation.get_object()['/C']:
                            color = annotation.get_object()['/C']
                            # Check if color is not red [1,0,0] or blue [0,0,1]
                            if color != [1,0,0] and color != [0,0,1]:
                                comment['clc'] = 1
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
                print(f"updating  page {str(comment['pageno'])} word {str(comment['wordindex'])} -  {str(comment['wordsno'])}")  
                if wordindex and wordsno:
                    c.execute(
                        "UPDATE wordsall SET x = ?, /* y = ?, */ width = ?, clc = ? WHERE wordindex = ? AND wordsno = ?",
                        (
                            (x1 - xshift) / 443.0,  # Normalize x
                            # 1 - (y1 - 81.0) / 691.0,  # Normalize y
                            (x2 - x1) / 443.0,  # Calculate width
                            comment.get('clc', 0),  # Get clc value, default to 0 if not present
                            wordindex,
                            wordsno
                        )
                    )
        except Exception as e:
            pass

    conn.commit()
    conn.close()
def adjust_line_positions():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Retrieve all rows ordered by wordindex
    c.execute("SELECT wordindex, wordsno, x, width, clc FROM wordsall ORDER BY wordindex")
    rows = c.fetchall()

    if not rows:
        print("No rows found.")
        conn.close()
        return

    margin = 0.01  # Define the margin

    # Helper function to find the nearest prior and next rows with clc == 0 or NULL
    def find_neighbors(index):
        prior = None
        next_ = None

        # Search backward for the prior row
        for j in range(index - 1, -1, -1):
            if rows[j][4] in (0, None):  # clc == 0 or NULL
                prior = rows[j]
                break

        # Search forward for the next row
        for j in range(index + 1, len(rows)):
            if rows[j][4] in (0, None):  # clc == 0 or NULL
                next_ = rows[j]
                break

        return prior, next_

    # Process each row
    for i, row in enumerate(rows):
        wordindex, wordsno, x, width, clc = row

        # Skip rows that don't need updating
        if clc != 1:
            continue

        # Find the prior and next neighbors
        prior, next_ = find_neighbors(i)

        # Calculate new x and width
        if prior and next_:
            new_x = prior[2] + prior[3] + margin  # Align with prior's right edge + margin
            new_width = max(next_[2] - margin - new_x, 0)  # Align with next's left edge - margin
        else:
            # If no valid neighbors found, skip update
            print(f"Skipping update for wordindex {wordindex}, wordsno {wordsno}: no valid neighbors.")
            continue

        # Update the row in the database
        c.execute(
            "UPDATE wordsall SET x = ?, width = ? WHERE wordindex = ? AND wordsno = ?",
            (new_x, new_width, wordindex, wordsno)
        )

        print(f"Updated wordindex {wordindex}, wordsno {wordsno}: x = {new_x}, width = {new_width}")

    conn.commit()
    conn.close()
    print("Adjustment process completed.")

script_path = os.path.abspath(__file__)
drive, _ = os.path.splitdrive(script_path) 
drive = drive + '/'

# Construct the database path correctly
db_path = os.path.join(drive, 'Qeraat', 'QeraatFasrhTools', 'QeraatSearch', 'qeraat_data_simple.db')

# Define the path for the qaree PDF file
qaree_file = os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'Musshaf', 'ShmrlyWords.pdf')

if os.path.exists(qaree_file):
    comments = extract_line_comments(qaree_file)
    update_words_xyw(comments)
    print("Line comments extracted and inserted from", qaree_file)
else:
    print("File not found:", qaree_file)

adjust_line_positions()