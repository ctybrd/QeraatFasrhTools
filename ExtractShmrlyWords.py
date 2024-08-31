import os
import shutil
import sqlite3
import re
from PyPDF2 import PdfReader
import webcolors
script_path = os.path.abspath(__file__)
drive, _ = os.path.splitdrive(script_path) 
drive = drive +'/'
db_path = os.path.join(drive, '/Qeraat/QeraatFasrhTools/QeraatSearch', 'qeraat_data_simple.db')
qaree_files = {
    "9": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'Musshaf', 'ShmrlyWords.pdf'),
}

def extract_line_comments(pdf_path):
    #column style (S = solid D =dashed H hollow circle)
    #column circle (empty = line only 1= line with right circle 2 = line with left circle 4 circle only for future use 3 will be center circle of the line )
    comments = []
    pdf = PdfReader(pdf_path)

    for pageno, page in enumerate(pdf.pages):
        #for test
        # if pageno >= 3:
        #      break  # Exit the loop after processing the 7th page
        try:
            annotations = page['/Annots']        
            if annotations:
                for annotation in annotations:
                    if isinstance(annotation, str):
                        annotation = pdf.get_object(annotation)
                    elif isinstance(annotation, dict):
                        annotation = pdf._buildIndirectObject(annotation)
                    # print(annotation.get_object()['/Subtype'])
                    if annotation.get_object()['/Subtype'] == '/Line':
                        comment = {
                            'content': ' ',
                            'pageno': pageno+1,
                            'coordinates': annotation.get_object()['/Rect'],
                            'color': annotation.get_object()['/C']
                        }
                        comment['style'] = 'S'
                        comment['circle'] = ''
                        if '/BS' in annotation.get_object():
                            if '/S' in annotation.get_object()['/BS']:
                                comment['style'] = str(annotation.get_object()['/BS']['/S'])
                        if comment['style']=='/D':
                            comment['style'] = 'D'
                        if '/LE' in annotation.get_object():
                            if(str(annotation.get_object()['/LE'])) == "['/Circle', '/None']":
                                comment['circle'] ='2'
                            elif (str(annotation.get_object()['/LE'])) == "['/None', '/Circle']":
                                comment['circle'] ='1'
                        comments.append(comment)
                        
                    if annotation.get_object()['/Subtype'] == '/Circle':
                        comment = {
                            'content': ' ',
                            'pageno': pageno + 1,
                            'coordinates': annotation.get_object()['/Rect'],
                            'color': annotation.get_object()['/C']
                        }
                        # print(annotation.get_object())
                        comment['style'] = 'S'
                        comment['circle'] = '4'
                        # if '/BS' in annotation.get_object():
                        #     if '/S' in annotation.get_object()['/BS']:
                        #         comment['style'] = str(annotation.get_object()['/BS']['/S'])
                        
                        # Check if the oval fill color is none
                        # if '/MK' in annotation.get_object() and '/BG' in annotation.get_object()['/MK']:
                        if '/IC' in annotation.get_object():
                            fill_color = annotation.get_object()['/IC']
                            if fill_color == '[0 0 0]':
                                comment['style'] = 'H'
                        else:
                            comment['style'] = 'H'
                        
                        comments.append(comment)
                    
                        
        except Exception as e:
            # print(f"Error processing annotations on page {pageno}: {e}")
            pass


    return comments


def insert_comments_sqlite(comments,qaree_key):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # Delete rows with value "A" in the field "qaree"
    c.execute("DELETE FROM shmrly_words WHERE qaree = ?", (qaree_key,))
    xshift = 81.0
    
    for comment in comments:
        # print(comment['content'], comment['coordinates'], comment['color'])

        coordinates = str(comment['coordinates'])
        matches = re.findall(r'(\d+\.?\d*)', coordinates)
        x1, y1, x2, y2 = matches

        color_values = get_color_name(str(comment['color']),qaree_key)
        c.execute("INSERT INTO shmrly_words(qaree, page_number, color, x, y, width,style,circle) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (qaree_key, comment['pageno'], str(color_values), float((float(x1)-xshift)/443.0), 1-(float((float(y1)-81.0)/691.0)),max(0.05, float((float(x2) - float(x1)) / 443.0)),str(comment['style']),str(comment['circle'])))  # Use converted values
    c.execute("UPDATE shmrly_words SET style='S' where style is null")
    c.execute("UPDATE shmrly_words SET circle='' where circle is null")

    conn.commit()
    conn.close()

import webcolors


def get_color_name(color_values,qaree_key):
    fraction_values = eval(color_values)
    rgb_values_original = tuple(int(round(val * 255)) for val in fraction_values)
    color_name = '#{:02x}{:02x}{:02x}'.format(*rgb_values_original) 
    return color_name




def get_color_type(color_values):
    return ""


def process_qaree_key(qaree_key):
    pdf_path = qaree_files[qaree_key]
    if os.path.exists(pdf_path):
        comments = extract_line_comments(pdf_path)
        insert_comments_sqlite(comments, qaree_key)
        print("Line comments extracted and inserted from", pdf_path)
    else:
        print("File not found:", pdf_path)

def update_line_numbers(threshold=0.03):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # Retrieve all entries, grouped by page
    c.execute("SELECT id, page_number, y FROM shmrly_words WHERE qaree = ? ORDER BY page_number, y", (qaree_key,))
    rows = c.fetchall()
    
    current_page = None
    current_lineno = 0
    previous_y = None
    
    for row in rows:
        entry_id, page_number, y = row
        
        if page_number != current_page:
            current_page = page_number
            current_lineno = 1
            previous_y = y
        else:
            # Check if the difference in y is below the threshold
            if abs(y - previous_y) > threshold:
                current_lineno += 1
            previous_y = y
        
        # Update the lineno for the current entry
        c.execute("UPDATE shmrly_words SET lineno = ? WHERE id = ?", (current_lineno, entry_id))
    
    conn.commit()
    conn.close()


qaree_key = '9'
if qaree_key == "":
    qaree_key= "9"
process_qaree_key(qaree_key)

update_line_numbers()
conn = sqlite3.connect(db_path)
c = conn.cursor()

update_aya_heads ="""
WITH OrderedShmrlyWords AS (
    SELECT 
        ROW_NUMBER() OVER (ORDER BY page_number, lineno, x DESC) AS rn,
        id
    FROM 
        shmrly_words
    WHERE 
        color = '#0000ff'
),
OrderedBookQuran AS (
    SELECT 
        ROW_NUMBER() OVER (ORDER BY aya_index) AS rn,
        sora,
        aya
    FROM 
        book_quran
)
UPDATE shmrly_words
SET 
    surahno = obq.sora,
    ayahno = obq.aya
FROM 
    OrderedShmrlyWords osw
JOIN 
    OrderedBookQuran obq 
ON 
    osw.rn = obq.rn
WHERE 
    shmrly_words.id = osw.id
    AND shmrly_words.color = '#0000ff';
"""
conn.close
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute(update_aya_heads)
conn.commit()

update_surah_ayah ="""
WITH OrderedShmrlyWords AS (
    SELECT 
        id,
        color,
        surahno,
        ayahno,
        page_number,
        lineno,
        x,
        ROW_NUMBER() OVER (ORDER BY page_number, lineno, x DESC) AS rn
    FROM 
        shmrly_words
),
RedRows AS (
    SELECT 
        osw_red.id AS red_id,
        osw_red.rn AS red_rn,
        osw_red.page_number,
        osw_red.lineno,
        osw_red.x,
        MIN(osw_blue.rn) AS blue_rn
    FROM 
        OrderedShmrlyWords osw_red
    JOIN 
        OrderedShmrlyWords osw_blue
    ON 
        osw_red.page_number = osw_blue.page_number
        AND osw_blue.color = '#0000ff'
        AND osw_red.rn < osw_blue.rn
    WHERE 
        osw_red.color = '#ff0000'
    GROUP BY 
        osw_red.id, osw_red.rn, osw_red.page_number, osw_red.lineno, osw_red.x
)
UPDATE shmrly_words
SET 
    surahno = osw_blue.surahno,
    ayahno = osw_blue.ayahno
FROM 
    RedRows red
JOIN 
    OrderedShmrlyWords osw_blue 
ON 
    red.blue_rn = osw_blue.rn
WHERE 
    shmrly_words.id = red.red_id;

"""
conn.close
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute(update_surah_ayah)
conn.commit()

update_words_sql = """
WITH OrderedShmrlyWords AS (
    SELECT 
        ROW_NUMBER() OVER (ORDER BY page_number, lineno , x DESC) AS rn,
        qaree,
        page_number,
        color,
        x,
        y,
        width,
        style,
        circle,
        wordindex,
        rawword
    FROM 
        shmrly_words 
    WHERE 
        color = '#ff0000'
),
OrderedWords1 AS (
    SELECT 
        ROW_NUMBER() OVER (ORDER BY wordindex) AS rn,
        wordindex,
        rawword
    FROM 
        words1
)
UPDATE shmrly_words
SET 
    wordindex = ow.wordindex,
    rawword = ow.rawword
FROM 
    OrderedShmrlyWords osw
JOIN 
    OrderedWords1 ow 
ON 
    osw.rn = ow.rn
WHERE  
    shmrly_words.color = '#ff0000'
    AND shmrly_words.qaree = osw.qaree
    AND shmrly_words.page_number = osw.page_number
    AND shmrly_words.x = osw.x
    AND shmrly_words.y = osw.y;

"""
conn.close
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute(update_words_sql)
conn.commit()
conn.close()
# SELECT * from shmrly_words order by page_number, lineno , x DESC
print("All Done")