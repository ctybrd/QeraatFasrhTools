import sqlite3
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def add_lines_from_sqlite(input_pdf, output_pdf, db_file, line_width=1):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT page_number, color, x, y, width FROM madina_temp")
    data = cursor.fetchall()
    conn.close()

    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page_num in range(len(reader.pages)):
        page_num1 = page_num + 1
        page = reader.pages[page_num]
        page_width, page_height = float(page.mediabox.upper_right[0]), float(page.mediabox.upper_right[1])
        page_width1 = 254
        page_height1 = 412
        xmargin = 88 if page_num1 % 2 == 0 else 40
        ymargin = 67

        for row in data:
            if row[0] == page_num1:
                if row[2] is None or row[3] is None or row[4] is None:
                    continue  # Skip if any necessary value is None
                
                x = float(row[2]) * page_width1 + xmargin
                y = (1 - float(row[3])) * page_height1 + ymargin
                width = float(row[4]) * page_width1

                # Create a line annotation (adjust line height as needed)
                packet = io.BytesIO()
                can = canvas.Canvas(packet, pagesize=letter)
                can.setLineWidth(line_width)  # Set the line thickness

                # Check if the color is valid
                try:
                    color = tuple(int(row[1][i:i+2], 16) / 255 for i in (1, 3, 5))
                    can.setStrokeColorRGB(*color)  # Convert hex color to RGB
                except Exception as e:
                    print(f"Invalid color {row[1]} at row {row}: {e}")
                    continue

                can.line(x, y, x + width, y)
                can.save()

                packet.seek(0)
                new_pdf = PdfReader(packet)
                page.merge_page(new_pdf.pages[0])

        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

# Example usage with line thickness set to 3
add_lines_from_sqlite("D:/Qeraat/Madina.pdf", "D:/Qeraat/Madina_wlines.pdf", "D:/Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db", line_width=3)
