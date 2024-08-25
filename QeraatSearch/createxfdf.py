import sqlite3
import uuid
import datetime
import os
edition ='M'
def create_xfdf(output_xfdf, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    table_name ='madina_temp' if edition == 'M' else 'shmrly_temp'
    cursor.execute(f'SELECT page_number, color, x, y, width, style, circle FROM {table_name}')
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
        else: #shamarly
            page_width = 595.22
            page_height = 842

            page_width1 = 446
            page_height1 = 693
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
        creation_date = datetime.datetime.now().strftime("D:%Y%m%d%H%M%S+03'00'")
        annot_name = str(uuid.uuid4())

        # Determine the additional attribute based on the circle value
        additional_attribute = ''
        if circle == "1":
            additional_attribute = ' tail="Circle"'
        elif circle == "2":
            additional_attribute = ' head="Circle"'
        if style == 'D':
            additional_attribute +='style="dash" dashes="3,3"'
        if circle != "4":
            annot = f'''
            <line start="{x_start},{y_start}" end="{x_end},{y_end}" title="Me" creationdate="{creation_date}" subject="Line" page="{page_number}" date="{creation_date}" flags="print" name="{annot_name}" rect="{x_start},{y_start - 0.5},{x_end},{y_start + 0.5}" color="{color}" interior-color="{color}"{additional_attribute} endingScale="0.7,0.7" width="4"/>
            '''
        else:
            annot = f'''
            <circle {'interior-color="' + color + '" ' if style != 'H' else ''}title="Title" creationdate="{creation_date}" subject="Subject" page="{page_number}" date="{creation_date}" opacity="0.7" flags="print" name="{annot_name}" rect="{x_start},{y_start},{x_start+6},{y_start+6}" color="{color}" width="1"/>
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
drive = drive +'/'

create_xfdf( drive+"Qeraat/output_annots.xfdf", drive+"Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db")
