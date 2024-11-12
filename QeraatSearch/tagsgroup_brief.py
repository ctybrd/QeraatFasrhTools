import sqlite3
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Cm, RGBColor  # To set margins
from docx.oxml.ns import qn  # For reducing row spacing

# Connect to the SQLite database
conn = sqlite3.connect('D:\\Qeraat\\QeraatFasrhTools\\QeraatSearch\\qeraat_data_simple.db')
cursor = conn.cursor()

# Updated SQL query with GROUP BY
query = """WITH RECURSIVE tags_split(aya_index, id, sub_subject, reading, qareesrest, tag, remaining_tags) AS (
    -- Base case: Initial split
    SELECT aya_index, id, sub_subject, reading, qareesrest,
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

    -- Recursive case: Continue splitting the remaining tags
    SELECT aya_index, id, sub_subject, reading, qareesrest,
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

-- Final query with JOINs and filtering
SELECT page_shmrly, description, reading, group_concat(distinct sub_subject) AS sub_subject, 
       group_concat(distinct qareesrest) AS qareesrest
FROM (
    SELECT ts.aya_index, 
           ts.id, 
           ts.sub_subject, 
           ts.reading, 
           ts.tag, 
           tm.description,
           tm.category,
           qd.page_shmrly,
           qd.sora,
           qd.aya, 
           qd.qareesrest
    FROM tags_split ts
    LEFT JOIN tagsmaster tm ON ts.tag = tm.tag
    JOIN quran_data qd ON ts.aya_index = qd.aya_index AND ts.id = qd.id
    WHERE ts.tag != '' 
      AND ts.tag != 'meemsela' 
      AND ts.tag != 'waqfhesham' 
      AND ts.tag != 'waqfhamza'
    ORDER BY qd.page_shmrly, ts.tag, ts.aya_index, ts.id
)
GROUP BY page_shmrly, tag, description, reading;

"""

# Fetch data
data = cursor.execute(query).fetchall()
conn.close()

# Create a new Word document
doc = Document()

# Set page margins to 0.7 cm
section = doc.sections[0]
section.top_margin = Cm(0.7)
section.bottom_margin = Cm(0.7)
section.left_margin = Cm(0.7)
section.right_margin = Cm(0.7)

# Variable to track the last page_shmrly for conditional page breaks
last_page_shmrly = None

# Generate the document
for row in data:
    page_shmrly = row[0]  # page_shmrly
    description = row[1]   # description
    reading = row[2]       # reading
    sub_subjects = row[3]  # sub_subject
    qareesrests = row[4]   # qareesrest

    # Check if we need a page break
    if last_page_shmrly is None or page_shmrly != last_page_shmrly:
        if last_page_shmrly is not None:  # Add a page break only if it's not the first page
            doc.add_page_break()
        
        # Update the last_page_shmrly
        last_page_shmrly = page_shmrly  
        
        # Add a header with the page number
        doc.add_heading(f'صفحة: {page_shmrly}', level=1).alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    # Add tag description
    doc.add_heading(description, level=2)

    # Create a table for the records
    table = doc.add_table(rows=1, cols=4)  # 4 columns for page_shmrly, description, reading, qareesrest
    
    # Set column widths
    table.columns[0].width = int(1.5 * 914400)  # 1.5 cm for Aya
    table.columns[1].width = int(3.0 * 914400)  # 3 cm for Sub Subject
    table.columns[2].width = int(5.0 * 914400)  # 5 cm for Reading
    table.columns[3].width = int(3.0 * 914400)  # 3 cm for Qareesrest
    
    # Create a new row
    row_cells = table.add_row().cells
    row_cells[0].text = str(page_shmrly)  # Page number
    cell_sub_subject = row_cells[1]
    cell_sub_subject.text = str(sub_subjects)  # Sub Subjects
    # Change the text color of the sub_subject cell to green
    for paragraph in cell_sub_subject.paragraphs:
        for run in paragraph.runs:
            run.font.color.rgb = RGBColor(0, 128, 0)  # Green color
    row_cells[2].text = str(reading)  # Reading
    row_cells[3].text = str(qareesrests)  # Qareesrest

    # Reduce the space between rows
    for cell in row_cells:
        paragraph = cell.paragraphs[0]
        paragraph_format = paragraph.paragraph_format
        paragraph_format.space_after = Cm(0)  # No space after each paragraph
        paragraph_format.space_before = Cm(0)  # No space before each paragraph

    doc.add_paragraph()  # Add a space before the next entry

# Save the document
doc.save('shmrly_osoul_brief.docx')
