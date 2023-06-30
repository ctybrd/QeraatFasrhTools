import io
import PyPDF2
from reportlab.pdfgen import canvas

def extract_comments(source_pdf_path):
    comments = []
    with open(source_pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_number, page in enumerate(reader.pages, 1):
            annotations = page.get('/Annots')
            if annotations:
                for annotation in annotations:
                    if annotation.get_object()['/Subtype'] == '/Text':
                        comments.append((page_number, annotation.get_object()['/Contents']))
    return comments

def add_comments_as_text_boxes(source_pdf_path, destination_pdf_path, comments):
    with open(source_pdf_path, 'rb') as source_file, open(destination_pdf_path, 'wb') as destination_file:
        reader = PyPDF2.PdfReader(source_file)
        writer = PyPDF2.PdfWriter()

        for page_number, page in enumerate(reader.pages, 1):
            writer.add_page(page)

            for comment_page_number, comment in comments:
                if comment_page_number == page_number:
                    x, y = 100, 100 + (page_number - 1) * 50  # Adjust the coordinates according to your needs
                    width, height = 300, 30  # Adjust the size of the text box
                    output_buffer = io.BytesIO()
                    c = canvas.Canvas(output_buffer)
                    c.setFont('Helvetica', 12)
                    c.drawString(x, y, comment)
                    c.rect(x, y - height, width, height, stroke=0, fill=0)  # Add a border around the text box
                    c.showPage()
                    c.save()
                    text_page = PyPDF2.PdfReader(output_buffer).pages[0]
                    writer.pages[page_number - 1].merge_page(text_page)

        writer.write(destination_file)

# Usage example
source_pdf_path = 'E:\Qeraat\Tayseer\Tayseer10.pdf'
destination_pdf_path = 'E:\Qeraat\Tayseer\Target.pdf'

comments = extract_comments(source_pdf_path)
add_comments_as_text_boxes(source_pdf_path, destination_pdf_path, comments)
