import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
from PyPDF2.generic import IndirectObject

pdf_path = 'e:/warsh_merge.pdf'
png_folder = 'E:/Qeraat/ShmrlySides/SideNew/'
output_path = 'e:/warsh_merge_output.pdf'

pdf = PdfReader(pdf_path)
pdf_writer = PdfWriter()

for i, page in enumerate(pdf.pages):
    png_path = f'{png_folder}/{i + 1}.png'  # Assuming your PNG files are named as 1.png, 2.png, etc.

    png_image = Image.open(png_path)
    png_pdf = png_image.convert('RGB')

    temp_pdf = PdfWriter()
    temp_pdf.add_blank_page(width=595, height=842)  # Set page size to A4

    image_obj = {
        '/Type': '/XObject',
        '/Subtype': '/Image',
        '/Width': png_pdf.width,
        '/Height': png_pdf.height,
        '/BitsPerComponent': 8,
        '/ColorSpace': '/DeviceRGB',
        '/Filter': '/FlateDecode',
        '/Length': len(png_pdf.tobytes()),
        '/Stream': png_pdf.tobytes(),
    }

    image_obj = IndirectObject(len(temp_pdf._objects) + 1, 0, temp_pdf)
    temp_pdf.add_object(image_obj)

    temp_pdf.add_page(page)
    temp_pdf.add_blank_page()  # Add a blank page

    reference_str = f"{image_obj.id} {image_obj.generation} R"  # Get the reference string for the image object
    content_stream = f"{reference_str} Do"
    temp_pdf.pages[-1].add_content_stream(content_stream)  # Add content stream to the last page

    for j in range(temp_pdf.numPages):
        pdf_writer.add_page(temp_pdf.getPage(j))

with open(output_path, 'wb') as output_file:
    pdf_writer.write(output_file)
