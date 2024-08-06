import sqlite3
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def add_lines_from_sqlite(input_pdf, output_pdf, db_file):
  conn = sqlite3.connect(db_file)
  cursor = conn.cursor()
  cursor.execute("SELECT page_number, color, x, y, width FROM madina_temp")
  data = cursor.fetchall()
  conn.close()

  reader = PdfReader(input_pdf)
  writer = PdfWriter()

  for page_num in range(len(reader.pages)):
    page = reader.pages[page_num]
    page_width, page_height = float(page.mediabox.upper_right[0]), float(page.mediabox.upper_right[1])
    
    for row in data:
      if row[0] == page_num:
        x = float(row[2]) * page_width
        y = float(row[3]) * page_height
        width = float(row[4]) * page_width

        # Create a line annotation (adjust line height as needed)
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setStrokeColorRGB(*tuple(int(row[1][i:i+2], 16) for i in (1, 3, 5)))  # Convert hex color to RGB

        can.line(x, y, x + width, y)
        can.save()

        packet.seek(0)
        new_pdf = PdfReader(packet)
        page.merge_page(new_pdf.pages[0])

    writer.add_page(page)

  with open(output_pdf, "wb") as f:
    writer.write(f)

# Example usage
add_lines_from_sqlite("D:/Qeraat/Madina.pdf", "D:/Qeraat/Madina_wlines.pdf", "D:/Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db")
