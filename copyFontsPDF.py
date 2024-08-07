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
        for fontno,font_info in enumerate(fonts):
            font_name = fonts[fontno][3]
            pdf_fonts.add(font_name)

    pdf_document.close()
    return pdf_fonts

def embed_fonts(source_pdf_path, target_pdf_path):
    source_fonts = extract_fonts(source_pdf_path)
    packet = io.BytesIO()
    can = canvas.Canvas(packet)

    # Load all fonts from the source PDF using reportlab
    for font_name in source_fonts:
        try:
            can.setFont(font_name, 12)
        except:
            print(f"Ignored font: {font_name}")

    can.save()

    # Move to the beginning of the buffer
    packet.seek(0)
    new_pdf = PyPDF2.PdfReader(packet)
    existing_pdf = PyPDF2.PdfReader(source_pdf_path)

    output = PyPDF2.PdfWriter()

    # Merge the two PDFs
    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.pages[i-1]
        page.mergePage(new_pdf.pages[-1])
        output.addPage(page)

    # Save the result to a new PDF
    with open(target_pdf_path, "wb") as f:
        output.write(f)


if __name__ == "__main__":
    source_pdf_path = "E:/Qeraat/QeraatFasrhTools_Data/Damrah_Hamzah.pdf"
    target_pdf_path = "E:/Qeraat/QeraatFasrhTools_Data/Hamzah-Shamarly-Shalaby.pdf"

    embed_fonts(source_pdf_path, target_pdf_path)
