import os
import shutil
import sqlite3
import re
from PyPDF2 import PdfReader
import webcolors


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

def update_surahno_ayahno():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Fetch all rows ordered by page_number, lineno, and x DESC
    c.execute("SELECT id, page_number, lineno, x, surahno, ayahno, color FROM shmrly_words ORDER BY page_number, lineno, x DESC")
    shmrly_rows = c.fetchall()

    # Fetch all rows from book_quran ordered by aya_index
    c.execute("SELECT sora, aya FROM book_quran ORDER BY aya_index")
    quran_rows = c.fetchall()

    quran_index = 0
    for shmrly_row in shmrly_rows:
        shmrly_id, page_number, lineno, x, surahno, ayahno, color = shmrly_row
       # Get the current quran data
        quran_sora, quran_aya = quran_rows[quran_index]
        # Update the surahno and ayahno in shmrly_words
        c.execute("""
            UPDATE shmrly_words 
            SET surahno = ?, ayahno = ? 
            WHERE id = ?
        """, (quran_sora, quran_aya, shmrly_id))
        if color == '#0000ff':
            # Skip to the next quran row after encountering a blue line
            quran_index += 1
            if quran_index >= len(quran_rows):
                break  # If no more quran rows, exit the loop
    conn.commit()
    conn.close()

import sqlite3

def update_words():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Fetch distinct surahno and ayahno from shmrly_words
    c.execute("SELECT DISTINCT surahno, ayahno FROM shmrly_words WHERE color='#ff0000' ORDER BY surahno, ayahno")
    distinct_rows = c.fetchall()

    for surahno, ayahno in distinct_rows:
        # Fetch rows from shmrly_words with the current surahno and ayahno
        c.execute("""
            SELECT id, surahno, ayahno, color 
            FROM shmrly_words 
            WHERE surahno = ? AND ayahno = ? AND color='#ff0000'
            ORDER BY page_number, lineno, x DESC
        """, (surahno, ayahno))
        shmrly_rows = c.fetchall()

        # Fetch rows from words1 with the current surah and ayah
        c.execute("""
            SELECT wordindex, surah, ayah, wordsno, word, rawword, nextword 
            FROM words1 
            WHERE surah = ? AND ayah = ? 
            ORDER BY wordindex
        """, (surahno, ayahno))
        words1_rows = c.fetchall()

        words1_index = 0
        for shmrly_row in shmrly_rows:
            shmrly_id, surahno, ayahno, color = shmrly_row

            # Ensure we are within the bounds of words1 rows
            if words1_index >= len(words1_rows):
                break

            words1_row = words1_rows[words1_index]
            wordindex, surah, ayah, wordsno, word, rawword, nextword = words1_row

            # Check if the surah and ayah match
            if surah == surahno and ayah == ayahno:
                # Update the shmrly_words table with the corresponding wordindex and rawword
                c.execute("""
                    UPDATE shmrly_words
                    SET wordindex = ?, rawword = ?
                    WHERE id = ?
                """, (wordindex, rawword, shmrly_id))

                # Move to the next words1 row
                words1_index += 1
            else:
                # If they don't match, skip updating shmrly_words and continue with the next iteration          
                continue

    conn.commit()
    conn.close()


script_path = os.path.abspath(__file__)
drive, _ = os.path.splitdrive(script_path) 
drive = drive + '/'

# Construct the database path correctly
db_path = os.path.join(drive, 'Qeraat', 'QeraatFasrhTools', 'QeraatSearch', 'qeraat_data_simple.db')

# Define the path for the qaree PDF file
qaree_files = {
    "9": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'Musshaf', 'ShmrlyWords.pdf'),
}

# Define the key for the qaree file
qaree_key = '9'
if qaree_key == "":
    qaree_key = "9"

# Process the qaree file and insert comments into the SQLite database
process_qaree_key(qaree_key)

# Update the line numbers
update_line_numbers()

# Order the rows by page_number, lineno, and x DESC
update_ordr_field = """
WITH OrderedRows AS (
  SELECT
    id,
    ROW_NUMBER() OVER (ORDER BY page_number, lineno, x DESC) AS row_num
  FROM shmrly_words
)
UPDATE shmrly_words
SET ordr = (
  SELECT row_num
  FROM OrderedRows
  WHERE OrderedRows.id = shmrly_words.id
);
"""

# Execute the ordering SQL command
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute(update_ordr_field)
conn.commit()
conn.close()

# Update surahno and ayahno fields
update_surahno_ayahno()
update_words()

# Test the queries
test_str = "SELECT * from shmrly_words order by page_number, lineno , x DESC"
test_str2 = """select s.surahno,s.ayahno,w.surah,ayah,s.* from shmrly_words s left join words1 w on s.wordindex=w.wordindex
where s.surahno<>w.surah or  s.ayahno<>w.ayah"""
print(test_str, test_str2)
print("All Done")
test_matching="""
select * from(
WITH ShmrlyCounts AS (
    SELECT
        surahno AS surah,
        ayahno AS ayah,
        COUNT(*) AS row_count_shmrly
    FROM
        shmrly_words
--     WHERE
--         color = '#ff0000'
    GROUP BY
        surahno,
        ayahno
),
Words1Counts AS (
    SELECT
        surah AS surah,
        ayah AS ayah,
        COUNT(*) AS row_count_words1
    FROM
        words1
    GROUP BY
        surah,
        ayah
)
SELECT
    sc.surah,
    sc.ayah,
    sc.row_count_shmrly,
    wc.row_count_words1,
    CASE
        WHEN sc.row_count_shmrly = wc.row_count_words1+1 THEN 'Match'
        ELSE 'Mismatch'
    END AS count_status
FROM
    ShmrlyCounts sc
LEFT JOIN
    Words1Counts wc
ON
    sc.surah = wc.surah
    AND sc.ayah = wc.ayah

UNION

SELECT
    wc.surah,
    wc.ayah,
    sc.row_count_shmrly,
    wc.row_count_words1,
    CASE
        WHEN sc.row_count_shmrly = wc.row_count_words1+1 THEN 'Match'
        ELSE 'Mismatch'
    END AS count_status
FROM
    Words1Counts wc
LEFT JOIN
    ShmrlyCounts sc
ON
    wc.surah = sc.surah
    AND wc.ayah = sc.ayah
) T

where row_count_shmrly is not NULL
and count_status='Mismatch'"""

update_line="""
SELECT
  id,
  y,
  page_number,rawword,
  lineno,
  CAST(((y * 2189.0)-65.0) / 145.93 AS INTEGER)+1  AS predicted_line
FROM shmrly_words
where lineno<>predicted_line
order by page_number,predicted_line ;
WITH updated_lines AS (
  SELECT
    id,
    CAST(((y * 2189.0) - 65.0) / 145.93 AS INTEGER) + 1 AS predicted_line
  FROM shmrly_words
)
UPDATE shmrly_words
SET reallineno = (
  SELECT predicted_line
  FROM updated_lines
  WHERE shmrly_words.id = updated_lines.id
);

"""