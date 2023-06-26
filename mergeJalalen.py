import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def paste_image_on_pdf(pdf_file, image_folder):
    pdf_writer = PyPDF2.PdfWriter()

    file = open(pdf_file, 'rb')
    pdf_reader = PyPDF2.PdfReader(file)
    total_pages = len(pdf_reader.pages)

    for i in range(1, total_pages + 1):
        page = pdf_reader.pages[i - 1]  # Adjusting for 0-based indexing

        if 2 <= i <= 522:  # Assuming the images are numbered from 2 to 522
            image_path = f'{image_folder}/{i}.jpg'  # Assuming the images are in a folder named 'image_folder'

            # Determine the desired location on the page to place the image (adjust these values as needed)
            if i % 2 == 0:  # Even pages
                x = 60  # X-coordinate of the image placement
                y = 196  # Y-coordinate of the image placement
            else:  # Odd pages
                x = 204  # X-coordinate of the image placement
                y = 210  # Y-coordinate of the image placement

            # Open the page in ReportLab canvas
            c = canvas.Canvas(f'temp_page_{i}.pdf', pagesize=letter)

            # Draw the image on the canvas
            c.drawImage(image_path, x, y, width=260, preserveAspectRatio=True)

            # Save the canvas as a PDF
            c.save()

            # Read the PDF with the image
            with open(f'temp_page_{i}.pdf', 'rb') as temp_file:
                temp_reader = PyPDF2.PdfReader(temp_file)
                pdf_writer.add_page(temp_reader.pages[0])

    # Write the final PDF
    with open('final.pdf', 'wb') as output:
        pdf_writer.write(output)

    # Close the original PDF file
    file.close()

# Usage
pdf_file = 'e:/qeraat/Jalaen_Shmrly.pdf'  # Replace with your input PDF file
image_folder = 'e:/Qeraat/PagesBook'  # Replace with the folder path containing the images
paste_image_on_pdf(pdf_file, image_folder)
