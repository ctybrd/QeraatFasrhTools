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
                        "UPDATE wordsall SET x = ?, y = ?, width = ? WHERE wordindex = ? AND wordsno = ?",
                        (
                            (x1 - xshift) / 443.0,  # Normalize x
                            1 - (y1 - 81.0) / 691.0,  # Normalize y
                            (x2 - x1) / 443.0,  # Calculate width
                            wordindex,
                            wordsno
                        )
                    )
        except Exception as e:
            pass

    conn.commit()
    conn.close()

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
