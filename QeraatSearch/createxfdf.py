import sqlite3
import uuid
import datetime
import os

edition = 'W'

def create_xfdf(output_xfdf, db_file):
    color_tracker = {}
    word_counts_by_line_and_page = {}
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Determine the table name
    if edition == 'M':
        table_name = 'madina_temp'
    elif edition == 'S':
        table_name = 'shmrly_temp'
    elif edition == 'A':
        table_name = 'shmrly_words'
    elif edition == 'W':
        table_name = 'wordsall'

    # Query data
    if edition == 'W':
        xsql = """
        SELECT page_number2 AS page_number,
               CASE WHEN wordsno < 999 THEN '#ff0000' ELSE '#0000ff' END AS color,
               x, y, width, 'S' AS style, '' AS circle, rawword, wordindex, wordsno, surah, ayah, lineno2
        FROM wordsall
        ORDER BY page_number2, lineno2, wordindex, wordsno
        """
    else:
        xsql = f"""
        SELECT page_number, color, x, y, width, style, circle, rawword,
               0 AS wordindex, 0 AS wordsno, 0 AS surah, 0 AS ayah, 0 AS lineno2
        FROM {table_name}
        """
    cursor.execute(xsql)
    data = cursor.fetchall()
    conn.close()

    # Precompute word counts for each line (`lineno2`) on each page
    for row in data:
        page_number = row[0]
        lineno2 = row[12]
        key = (page_number, lineno2)
        if key not in word_counts_by_line_and_page:
            word_counts_by_line_and_page[key] = 0
        word_counts_by_line_and_page[key] += 1

    # Create annotations
    annots = []
    for row in data:
        page_number = row[0] - 1  # PDF pages are 0-indexed
        if row[2] is None or row[3] is None or row[4] is None:
            continue  # Skip invalid rows

        # Page layout
        if edition == 'M':
            page_width, page_height = 382, 547
            page_width1, page_height1 = 254, 412
            xmargin = 88 if (page_number + 1) % 2 == 0 else 40
            ymargin = 67
        else:  # Shamarly
            page_width, page_height = 595.22, 842
            page_width1, page_height1 = 446, 693
            xmargin = 80 if (page_number + 1) % 2 == 0 else 84
            ymargin = 80

        # Calculate positions
        x = float(row[2]) * page_width1 + xmargin
        y = (1 - float(row[3])) * page_height1 + ymargin
        width = float(row[4]) * page_width1
        x_start, y_start = max(0, min(x, page_width)), max(0, min(y, page_height))
        x_end, y_end = max(0, min(x + width, page_width)), y_start

        # Handle color alternation and reset by page and line
        lineno2 = row[12]
        key = (page_number, lineno2)
        if key not in color_tracker:
            color_tracker[key] = 0  # Initialize tracker for this page-line combination

        total_words = word_counts_by_line_and_page.get(key, 0)
        if color_tracker[key] == 0:
            color = '#FF0000'  # First word red
        elif color_tracker[key] == total_words - 1:
            color = '#FF0000'  # Last word red
        elif color_tracker[key] % 2 == 1:
            color = '#90EE90'  # Alternating green
        else:
            color = '#FF0000'  # Alternating red

        color_tracker[key] += 1

        # Annotation details
        rawword = row[7]
        annot_name = f"{row[8]}-{row[9]}-{row[10]}-{row[11]}"
        creation_date = datetime.datetime.now().strftime("D:%Y%m%d%H%M%S+03'00'")
        additional_attribute = ''
        circle, style = row[6], row[5]
        if circle == "1":
            additional_attribute = ' tail="Circle"'
        elif circle == "2":
            additional_attribute = ' head="Circle"'
        if style == 'D':
            additional_attribute += ' style="dash" dashes="3,3"'

        # Line or circle annotation
        if circle != "4":
            annot = f'''
            <line start="{x_start},{y_start}" end="{x_end},{y_end}" title="{rawword}" creationdate="{creation_date}" subject="Line" page="{page_number}" date="{creation_date}" flags="print" name="{annot_name}" rect="{x_start},{y_start - 0.5},{x_end},{y_start + 0.5}" color="{color}" interior-color="{color}"{additional_attribute} endingScale="0.7,0.7" width="4">
            </line>
            '''
        else:
            annot = f'''
            <circle {'interior-color="' + color + '" ' if style != 'H' else ''}title="{rawword}" creationdate="{creation_date}" subject="Circle" page="{page_number}" date="{creation_date}" opacity="0.7" flags="print" name="{annot_name}" rect="{x_start},{y_start},{x_start + 8},{y_start + 8}" color="{color}" width="1">
            </circle>
            '''
        annots.append(annot)

    # Generate XFDF content
    xfdf_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<xfdf xmlns="http://ns.adobe.com/xfdf/" xml:space="preserve">
  <f href="https://t.me/ctybrd247"/>
  <ids original="{uuid.uuid4().hex}" modified="{uuid.uuid4().hex}"/>
  <annots>
    {''.join(annots)}
  </annots>
</xfdf>'''

    # Write XFDF file
    with open(output_xfdf, 'w', encoding='utf-8') as f:
        f.write(xfdf_content)

# Example usage
script_path = os.path.abspath(__file__)
drive, _ = os.path.splitdrive(script_path)
drive = drive + '/'

create_xfdf(drive + "Qeraat/output_annots.xfdf", drive + "Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db")
