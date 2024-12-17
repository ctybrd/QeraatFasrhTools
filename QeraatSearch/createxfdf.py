import sqlite3
import uuid
import datetime
import os
import html

edition = 'W'

def create_xfdf(output_xfdf, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    if edition == 'M':
        table_name = 'madina_temp'
    elif edition == 'S':
        table_name = 'shmrly_temp'
    elif edition == 'A':
        table_name = 'shmrly_words'
    elif edition == 'W':
        table_name = 'wordsall'

    if edition == 'W':
        xsql = f"SELECT page_number2 page_number, case when wordsno<999 then '#ff0000' else '#0000ff' end color, x, y, width, 'S' style, '' circle, rawword,wordindex,wordsno,surah,ayah FROM wordsall "
    else:
        xsql = f'SELECT page_number, color, x, y, width, style, circle, rawword,0 as wordindex,0 as wordsno,0 as surah,0 ayah FROM {table_name}'
    cursor.execute(xsql)
    data = cursor.fetchall()
    conn.close()

    annots = []
    for row in data:
        page_number = row[0] - 1
        
        if edition == 'M':
            page_width = 382
            page_height = 547

            page_width1 = 254
            page_height1 = 412
            xmargin = 88 if (page_number + 1) % 2 == 0 else 40
            ymargin = 67
        else:  # shamarly
            page_width = 595.22
            page_height = 842

            page_width1 = 446
            page_height1 = 693
            #yaqoob xmargin = 20 if (page_number + 1) % 2 == 0 else 124
            xmargin = 80 if (page_number + 1) % 2 == 0 else 84
            ymargin = 80

        if row[2] is None or row[3] is None or row[4] is None:
            continue  # Skip if any necessary value is None

        x = float(row[2]) * page_width1 + xmargin
        y = (1 - float(row[3])) * page_height1 + ymargin
        width = float(row[4]) * page_width1

        # Convert to PDF units (points)
        x_start = max(0, min(x, page_width))
        y_start = max(0, min(y, page_height))
        x_end = max(0, min(x + width, page_width))
        y_end = y_start

        color = row[1]
        circle = row[6]
        style = row[5]
        rawword = row[7]

        creation_date = datetime.datetime.now().strftime("D:%Y%m%d%H%M%S+03'00'")
        if edition == 'W':
            annot_name = str(row[8]) +'-' +str(row[9]) +'-' +str(row[10]) +'-' +str(row[11])
        else:
            annot_name = str(uuid.uuid4())

        # Escape the rawword and encode to HTML entities

        rawword_escaped = rawword #html.escape(rawword)

        # Create the contents-richtext XML snippet
        contents_richtext = ''
        # if rawword:
        #     contents_richtext = f'''
        #     <contents-richtext>
        #         <body xmlns="http://www.w3.org/1999/xhtml" 
        #             xmlns:xfa="http://www.xfa.org/schema/xfa-data/1.0/" 
        #             xfa:APIVersion="Acrobat:10.1.5" 
        #             xfa:spec="2.1" 
        #             style="text-align:left;font-family:Arial;font-size:12pt;font-weight:normal;font-style:normal;text-decoration:none;color:#000000;">
        #             <p><span>{rawword_escaped}</span></p>
        #         </body>
        #     </contents-richtext>
        #     '''

        # Determine the additional attribute based on the circle value
        additional_attribute = ''
        if circle == "1":
            additional_attribute = ' tail="Circle"'
        elif circle == "2":
            additional_attribute = ' head="Circle"'
        if style == 'D':
            additional_attribute += ' style="dash" dashes="3,3"'

        if circle != "4":
            annot = f'''
            <line start="{x_start},{y_start}" end="{x_end},{y_end}" title="{rawword}" creationdate="{creation_date}" subject="Line" page="{page_number}" date="{creation_date}" flags="print" name="{annot_name}" rect="{x_start},{y_start - 0.5},{x_end},{y_start + 0.5}" color="{color}" interior-color="{color}"{additional_attribute} endingScale="0.7,0.7" width="4">
                {contents_richtext}
            </line>
            '''
        else:
            annot = f'''
            <circle {'interior-color="' + color + '" ' if style != 'H' else ''}title="Title" creationdate="{creation_date}" subject="Subject" page="{page_number}" date="{creation_date}" opacity="0.7" flags="print" name="{annot_name}" rect="{x_start},{y_start},{x_start+8},{y_start+8}" color="{color}" width="1">
                {contents_richtext}
            </circle>
            '''

        annots.append(annot)

    xfdf_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<xfdf xmlns="http://ns.adobe.com/xfdf/" xml:space="preserve">
  <f href="https://t.me/ctybrd247"/>
  <ids original="{uuid.uuid4().hex}" modified="{uuid.uuid4().hex}"/>
  <annots>
    {''.join(annots)}
  </annots>
</xfdf>'''

    with open(output_xfdf, 'w', encoding='utf-8') as f:
        f.write(xfdf_content)

# Example usage
script_path = os.path.abspath(__file__)
drive, _ = os.path.splitdrive(script_path)
drive = drive + '/'

create_xfdf(drive + "Qeraat/output_annots.xfdf", drive + "Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db")
