import fitz 
import os
import shutil

# Mapping of letters to PDF file paths
qaree_files = {
    "W": 'Warsh-Asbahani-Shamarly-Shalaby.pdf',
    "I": 'IbnAmer-Shamarly-Shalaby.pdf',
    "T": 'shamarly10th.pdf',
    "J": 'AbuJaafar-Shamarly-Shalaby.pdf',
    "K": 'Qaloon-Shamarly-Shalaby.pdf',
    "U": 'AshabSela-Shamrly-Shalaby.pdf',
    "M": 'Hamzah-Shamarly-Shalaby.pdf',
    "B": 'IbnKatheer-Shmarly-Shalaby.pdf',
    "S": 'Sho3ba-Shamarly-Shalaby.pdf',
    "A": 'Warsh-Azraq-Shamarly-Shalaby.pdf',
    "R": 'Warsh-Azraq-Shamarly-Shalaby_Light.pdf',
    "E": 'Kisai-Shamarly-Shalaby.pdf',
    "F": 'Khalaf-Shamarly-Shalaby.pdf',
    "X": 'Kisai-Khalaf-Shamarly-Shalaby.pdf',
    "Y": 'Yaaqoub-Shamarly-Shalaby.pdf',
    "C": 'AbuAmro-Shamarly-Shalaby.pdf',
    "D": 'Dori-AbuAmro-Shamarly-Shalaby.pdf',
    "G": 'Sosi-AbuAmro-Shamarly-Shalaby.pdf',
    "L": 'Tawasot-Shamarly-Shalaby.pdf',
    "O": 'Asem_IbnAmer-Shamarly-Shalaby.pdf',
    "P": 'AbuAmro-Yaqoub-Shamarly-Shalaby.pdf',
}
#Function to empty folder
def empty_folder(folder_path):
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
script_path = os.path.abspath(__file__)
drive, _ = os.path.splitdrive(script_path)
drive = drive +'/'
input_folder = os.path.join(drive,'Qeraat/NewSides/PDF_Sides_FLAT')
output_folder = os.path.join(drive,'Qeraat/NewSides/')

# Get the list of PDF files in the input folder
pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

for pdf_file in pdf_files:
    pdf_path = os.path.join(input_folder, pdf_file)
    
    # Determine the output directory based on the mapping
    letter = None
    for key, value in qaree_files.items():
        if pdf_file == value:
            letter = key
            break
    
    if letter is None:
        print(f"Mapping not found for {pdf_file}")
        continue
    
    # Create output directory if it doesn't exist
    output_dir = os.path.join(output_folder, f'Side{letter}')
    os.makedirs(output_dir, exist_ok=True)
    empty_folder(output_dir)
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Convert each page to an image and save it
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        dlist = page.get_displaylist()
        pix = dlist.get_pixmap()
        output_image_path = os.path.join(output_dir, f'{page_num + 1}.png')
        pix.save(output_image_path)
        print(f'Saved: {output_image_path}')