import fitz  # PyMuPDF
import PyPDF2
from reportlab.pdfgen import canvas
import io
def extract_fonts(source_pdf_path):
    pdf_fonts = set()
    pdf_document = fitz.open(source_pdf_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        fonts = page.get_fonts()
        for font_info in fonts:
            font_name = font_info["name"]
            if font_name in fitz.getAvailableFonts():
                pdf_fonts.add(font_name)

    pdf_document.close()
    return pdf_fonts

def embed_fonts(source_pdf_path, target_pdf_path):
    source_fonts = extract_fonts(source_pdf_path)
    packet = io.BytesIO()
    can = canvas.Canvas(packet)

    # Load all fonts from the source PDF using reportlab
    for font_info in source_fonts:
        font_name = font_info["name"]
        can.setFont(font_name, 12)

    can.save()

    # Move to the beginning of the buffer
    packet.seek(0)
    new_pdf = PyPDF2.PdfFileReader(packet)
    existing_pdf = PyPDF2.PdfFileReader(source_pdf_path)

    output = PyPDF2.PdfFileWriter()

    # Merge the two PDFs
    for i in range(existing_pdf.getNumPages()):
        page = existing_pdf.getPage(i)
        page.mergePage(new_pdf.getPage(i))
        for font_info in source_fonts:
            font_name = font_info["name"]
            page.setFont(font_name, 12)
        output.addPage(page)

    # Save the result to a new PDF
    with open(target_pdf_path, "wb") as f:
        output.write(f)


if __name__ == "__main__":
    source_pdf_path = "E:/Qeraat/QeraatFasrhTools_Data/Damrah_Hamzah.pdf"
    target_pdf_path = "E:/Qeraat/QeraatFasrhTools_Data/Hamzah-Shamarly-Shalaby.pdf"

    embed_fonts(source_pdf_path, target_pdf_path)
