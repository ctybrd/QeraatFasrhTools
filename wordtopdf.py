import os
from win32com.client import Dispatch

def batch_convert_docx_to_pdf(input_folder, output_folder):
    """Convert all .docx files in a folder to PDF format."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    word = Dispatch("Word.Application")
    word.Visible = False

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".docx"):
            docx_path = os.path.join(input_folder, file_name)
            print(docx_path)
            pdf_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.pdf")

            try:
                doc = word.Documents.Open(docx_path)
                doc.SaveAs(pdf_path, FileFormat=17)  # FileFormat=17 corresponds to PDF
                doc.Close()
                print(f"Converted: {file_name} -> {os.path.basename(pdf_path)}")
            except Exception as e:
                print(f"Failed to convert {file_name}: {e}")

    word.Quit()
    print("Batch conversion complete.")

# Usage
input_folder = "D:\Qeraat\QeraatFasrhTools\output_documents"
output_folder = "D:\Qeraat\QeraatFasrhTools\output_documents"
batch_convert_docx_to_pdf(input_folder, output_folder)
