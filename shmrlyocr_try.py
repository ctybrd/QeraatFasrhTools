import os
import cv2
from PIL import Image
import pytesseract
import sqlite3

# Paths
images_folder = "E:/Qeraat/Uthman/images"  # Folder containing images
database_file = "E:/Qeraat/QeraatFasrhTools/QeraatSearch/uthman.db"  # SQLite database file

# SQLite setup
conn = sqlite3.connect(database_file)
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS TextLines (
        PageNumber INTEGER,
        LineNumber INTEGER,
        FirstTwoWords TEXT,
        FullLineContent TEXT
    )
''')
conn.commit()

# Preprocessing function for better OCR
def preprocess_image(image_path):
    # Load image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply binary thresholding
    _, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    
    # Denoising (optional, adjust kernel size as needed)
    denoised = cv2.medianBlur(thresholded, 3)
    
    return denoised

# Line segmentation function
def segment_lines(image_path):
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    line_height = height // 15  # Divide the image into 15 equal parts (15 lines per page)
    lines = []
    for i in range(15):
        y_start = i * line_height
        y_end = (i + 1) * line_height
        line = image[y_start:y_end, 0:width]
        lines.append(line)
    return lines

# Main processing loop
for page_number, image_file in enumerate(sorted(os.listdir(images_folder)), start=1):
    if image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff')):
        image_path = os.path.join(images_folder, image_file)
        
        # Preprocess the full image
        preprocessed_image = preprocess_image(image_path)
        
        # Segment the image into lines
        segmented_lines = segment_lines(image_path)
        
        for line_number, line_image in enumerate(segmented_lines, start=1):
            # Convert line image to PIL format for Tesseract
            pil_line_image = Image.fromarray(line_image)
            
            # OCR for the line
            custom_config = r'--psm 6 --oem 3'
            text = pytesseract.image_to_string(Image.open(image_path), lang='ara', config=custom_config)

            # text = pytesseract.image_to_string(pil_line_image, lang='ara', config='--psm 6')
            
            # Split line into words
            words = text.split()
            
            # Extract first two words and full line content
            if len(words) >= 2:
                first_two_words = " ".join(words[:2])
            elif words:
                first_two_words = words[0]
            else:
                first_two_words = ""
            
            # Insert into database
            cursor.execute('''
                INSERT INTO TextLines (PageNumber, LineNumber, FirstTwoWords, FullLineContent)
                VALUES (?, ?, ?, ?)
            ''', (page_number, line_number, first_two_words, text))
            conn.commit()

            # Debugging output (optional)
            print(f"Page {page_number}, Line {line_number}, First Two Words: {first_two_words}, Full Line: {text}")

# Close database connection
conn.close()
print(f"Processing complete! Results saved in {database_file}.")
