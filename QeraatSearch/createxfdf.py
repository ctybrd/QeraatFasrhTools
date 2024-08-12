import sqlite3
import uuid
import datetime
import fitz  # PyMuPDF

def create_xfdf(input_pdf, output_xfdf, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT page_number, color, x, y, width, style, circle FROM madina_temp")
    data = cursor.fetchall()
    conn.close()

    # Open the input PDF to get page dimensions
    doc = fitz.open(input_pdf)
    
    annots = []
    for row in data:
        page_number = row[0] - 1  # Adjust page index as PyMuPDF starts from 0
        page = doc[page_number]
        page_width = page.mediabox.width
        page_height = page.mediabox.height

        page_width1 = 254
        page_height1 = 412
        xmargin = 88 if (page_number + 1) % 2 == 0 else 40
        ymargin = 67

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
        if circle != "4":
            annot = f'''
            <line start="{x_start},{y_start}" end="{x_end},{y_end}" title="Me" creationdate="{creation_date}" subject="Line" page="{page_number}" date="{creation_date}" flags="print" name="{annot_name}" rect="{x_start},{y_start - 0.5},{x_end},{y_start + 0.5}" color="{color}" interior-color="{color}"{additional_attribute}/>
            '''
        else:
            annot = f'''
            <circle {'interior-color="' + color + '" ' if style != 'H' else ''}title="Title" creationdate="{creation_date}" subject="Subject" page="{page_number}" date="{creation_date}" opacity="0.7" flags="print" name="{annot_name}" rect="{x_start},{y_start},{x_start+6},{y_start+6}" color="{color}" width="1"/>
            '''



        annots.append(annot)

    xfdf_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<xfdf xmlns="http://ns.adobe.com/xfdf/" xml:space="preserve">
  <f href="{input_pdf}"/>
  <ids original="{uuid.uuid4().hex}" modified="{uuid.uuid4().hex}"/>
  <annots>
    {''.join(annots)}
  </annots>
</xfdf>'''  

    with open(output_xfdf, 'w', encoding='utf-8') as f:
        f.write(xfdf_content)

# Example usage
create_xfdf("d:/Qeraat/Madina.pdf", "d:/Qeraat/Madina_annots.xfdf", "d:/Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db")
