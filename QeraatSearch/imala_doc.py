from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import sqlite3

# Connect to the SQLite database
db_path = "D:\\Qeraat\\QeraatFasrhTools\\QeraatSearch\\qeraat_data_simple.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Define the SQL query
sql_query = """
WITH RECURSIVE tags_split(aya_index, id, sub_subject, reading, qareesrest, rasaya, tag, remaining_tags) AS (
    SELECT aya_index, id, sub_subject1 sub_subject, reading, qareesrest, rasaya,
           TRIM(',' || CASE 
               WHEN INSTR(TRIM(tags), ',') > 0 THEN SUBSTR(TRIM(tags), 1, INSTR(TRIM(tags), ',') - 1)
               ELSE TRIM(tags)
           END, ','),
           TRIM(',' || CASE 
               WHEN INSTR(TRIM(tags), ',') > 0 THEN SUBSTR(TRIM(tags), INSTR(TRIM(tags), ',') + 1)
               ELSE ''
           END, ',')
    FROM quran_data 
    WHERE tags IS NOT NULL AND tags NOT LIKE '%nochange%' AND page_shmrly IS NOT NULL

    UNION ALL

    SELECT aya_index, id, sub_subject, reading, qareesrest, rasaya,
           TRIM(',' || CASE 
               WHEN INSTR(TRIM(remaining_tags), ',') > 0 THEN SUBSTR(TRIM(remaining_tags), 1, INSTR(TRIM(remaining_tags), ',') - 1)
               ELSE TRIM(remaining_tags)
           END, ','),
           TRIM(',' || CASE 
               WHEN INSTR(TRIM(remaining_tags), ',') > 0 THEN SUBSTR(TRIM(remaining_tags), INSTR(TRIM(remaining_tags), ',') + 1)
               ELSE ''
           END, ',')
    FROM tags_split
    WHERE remaining_tags != ''
)

SELECT page_shmrly,
       CASE WHEN tag = 'imala' THEN 'بالإمالة' ELSE 'بالتقليل' END AS description,
       CASE WHEN reading LIKE '%بخلف%' THEN ' بخلف ' ELSE '' END AS kholf,
       GROUP_CONCAT(DISTINCT sub_subject) AS sub_subject,
       GROUP_CONCAT(DISTINCT qareesrest) AS qareesall,
       srt,
       CASE WHEN rasaya IS NOT NULL THEN 'رؤوس الآي' ELSE 'ما ليس برأس آية' END AS rasaya
FROM (
    SELECT ts.aya_index, ts.id, ts.sub_subject,
           CASE WHEN ts.tag = 'imala' THEN 'بالإمالة' ELSE 'بالتقليل' END ||
           CASE WHEN qd.reading LIKE '%بخلف%' THEN ' بخلف ' ELSE '' END AS reading,
           ts.tag, tm.description, tm.srt, qd.page_shmrly, qd.qareesrest,
           CASE WHEN ts.tag IN ('imala', 'taklel') THEN qd.rasaya ELSE 1 END AS rasaya
    FROM tags_split ts
    LEFT JOIN tagsmaster tm ON ts.tag = tm.tag
    JOIN quran_data qd ON ts.aya_index = qd.aya_index AND ts.id = qd.id
    WHERE ts.tag != '' AND ts.tag IN ('imala', 'taklel')
    ORDER BY qd.page_shmrly, qd.rasaya, tm.srt, ts.aya_index, ts.id
)
GROUP BY page_shmrly, rasaya, srt, description, kholf
ORDER BY page_shmrly, rasaya, srt, description, kholf;
"""

# Execute the SQL query
cursor.execute(sql_query)
rows = cursor.fetchall()

# Close the database connection
conn.close()

# Initialize variables for document creation
doc = Document()
current_page_shmrly = None
current_rasaya = None
file_count = 1

def save_and_create_new_doc():
    global doc, file_count
    doc.save(f'D:/Qeraat/مشروع العشر/shmrly_imalataklel_{file_count}.docx')
    file_count += 1
    doc = Document()

# Helper function to add formatted text
def add_text(paragraph, text, font_color, underline=False, bold=False, size=12):
    run = paragraph.add_run(text)
    run.font.color.rgb = RGBColor(*font_color)
    run.font.underline = underline
    run.font.bold = bold
    run.font.size = Pt(size)
    run.add_text(' ')  # Add space after each run

# Process each row
for row in rows:
    page_shmrly, description, kholf, sub_subject, qareesall, srt, rasaya = row

    # Add a header for new page_shmrly
    if page_shmrly != current_page_shmrly:
        doc.add_heading(f'صفحة: {page_shmrly}', level=1).alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        current_page_shmrly = page_shmrly
        current_rasaya = None  # Reset rasaya for new page

    para = doc.add_paragraph()

    # Add Rasaya if it has changed, otherwise leave a space
    if rasaya != current_rasaya:
        add_text(para, rasaya, font_color=(0, 0, 128), underline=True)
        current_rasaya = rasaya
    else:
        add_text(para, ' ', font_color=(0, 0, 0))  # Just add a space if rasaya is the same

    # Add Description, Kholf, Sub_subject, and Qareesall
    add_text(para, description, font_color=(0, 0, 0))
    add_text(para, kholf, font_color=(0, 0, 0))
    add_text(para, sub_subject, font_color=(0, 128, 0))
    add_text(para, qareesall, font_color=(0, 0, 0))

# Save the final document
save_and_create_new_doc()

"Document generation completed successfully."
