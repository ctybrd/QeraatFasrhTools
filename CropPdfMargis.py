import os
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfReader, PdfWriter
from PIL import Image

# Input PDF files and output folder paths
pdf_files = [
    "e:/Qeraat/Shmrly_BLANK_QALOON.pdf",
    "e:/Qeraat/Shmrly_BLANK_SHO3BA.pdf"
]

output_folders = [
    "e:/Qeraat/NewSides/Sidek",
    "e:/Qeraat/NewSides/SideS"
    # Add paths to the output folders here (one for each PDF)
]

# Custom coordinates for even and odd pages
even_page_coordinates =    (482, 47.5, 0, 37.8)
odd_page_coordinates =     (0, 47.5, 482, 37.8)

# Loop through each PDF file
for pdf_file, output_folder in zip(pdf_files, output_folders):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf = PdfReader(open(pdf_file, 'rb'))

    # Loop through each page in the PDF
    for page_num in range(len(pdf.pages)):
        print(page_num)
        page = pdf.pages[page_num]

        # Define coordinates for the current page based on even or odd
        if page_num % 2 == 0:
            # Even page: custom coordinates
            coordinates = even_page_coordinates
        else:
            # Odd page: custom coordinates
            coordinates = odd_page_coordinates

        # Crop the page using the custom coordinates
        page.cropbox.lower_left=(coordinates[0], coordinates[1])
        page.cropbox.upper_right=(coordinates[2], coordinates[3])

        # Create a new PDF with the modified page
        pdf_writer = PdfWriter()
        pdf_writer.add_page(page)

        # Export the modified page as a PNG file
        png_file = os.path.join(output_folder, f"page_{page_num + 1}.png")
        with open(png_file, 'wb') as png_output:
            pdf_writer.write(png_output)

print("PDFs cropped and exported to PNG successfully!")
