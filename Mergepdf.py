from PyPDF2 import PdfReader, PdfWriter

# Paths to the input PDF files
pdf_file1_path = 'F:/Qeraat/QeraatFasrhTools_Data/Musshaf/Kisai-Khalaf-Shamarly-Shalaby.pdf'
pdf_file2_path = 'F:/Qeraat/QeraatFasrhTools_Data/Musshaf/Yaaqoub-Shamarly-Shalaby.pdf'
output_pdf_path = 'F:/Mix/Kisai_Khalaf_Yaqoob.pdf'

# Create PDF readers for both files
pdf1_reader = PdfReader(pdf_file1_path)
pdf2_reader = PdfReader(pdf_file2_path)

# Ensure both PDFs have the same number of pages
assert len(pdf1_reader.pages) == len(pdf2_reader.pages), "PDF files have different number of pages"

# Create a PDF writer to write the output
pdf_writer = PdfWriter()
pdf_writer.add_page(pdf1_reader.pages[0])
# Interleave pages
num_pages = len(pdf1_reader.pages)
for i in range(1, num_pages, 2):
    # Add two pages from the first PDF
    pdf_writer.add_page(pdf1_reader.pages[i])
    if i + 1 < num_pages:
        pdf_writer.add_page(pdf1_reader.pages[i + 1])

    # Add two pages from the second PDF
    pdf_writer.add_page(pdf2_reader.pages[i])
    if i + 1 < num_pages:
        pdf_writer.add_page(pdf2_reader.pages[i + 1])

# Write the interleaved pages to the output PDF
with open(output_pdf_path, 'wb') as output_pdf:
    pdf_writer.write(output_pdf)

print(f"Successfully created interleaved PDF: {output_pdf_path}")
