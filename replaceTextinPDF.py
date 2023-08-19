import PyPDF2

def replace_text_in_textboxes(input_path, output_path, replacements):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        pdf_writer = PyPDF2.PdfFileWriter()

        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            if '/Annots' in page:
                for annot in page['/Annots']:
                    print(annot.getObject())
                    if annot.getObject()['/Subtype'] == '/FreeText':
                        if annot.getObject()['/Contents']:
                            field_value = annot.getObject()['/Contents']
                            updated_value = field_value

                            # Perform character replacements
                            for original_char, new_char in replacements.items():
                                updated_value = updated_value.replace(original_char, new_char)

                            # Update the field with the modified value
                            annot.getObject().update({
                                PyPDF2.generic.createStringObject('/V'): PyPDF2.generic.createStringObject(updated_value)
                            })

            pdf_writer.addPage(page)

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    input_pdf = "E:\Qeraat\Hamzah-Shamarly-Shalaby.pdf"
    output_pdf = "E:\Qeraat\output.pdf"
    replacements = {
        "ﭽ": " ",
        "ﭼ": " ",
        # Add more character replacements as needed.
    }
    replace_text_in_textboxes(input_pdf, output_pdf, replacements)
