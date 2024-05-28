import os
import cv2
import numpy as np
import shutil

# List of letters for folder names
letters = ["K", "J", "B", "S", "W", "I", "M", "A", "E", "F", "X", "C", "U", "Y","L"]

# Base folder path
script_path = os.path.abspath(__file__)
drive, _ = os.path.splitdrive(script_path)
drive = drive +'/'

# Define the base folder path
base_folder_path = os.path.join(drive, r'/Qeraat/NewSides/')


# Tolerance for white color removal
tolerance = 30  # Adjust this value based on your needs

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

# Iterate over the list of letters
for letter in letters:
    folder_path = os.path.join(base_folder_path, 'Side' + letter)
    
    # Create a new folder to save the modified images
    output_folder_path = os.path.join(base_folder_path, 'PNG', 'Side' + letter)
    os.makedirs(output_folder_path, exist_ok=True)
    empty_folder(output_folder_path)
    
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            file_path = os.path.join(folder_path, filename)

            # Read the image using OpenCV
            image = cv2.imread(file_path)

            # Convert the image to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Create a mask by thresholding the grayscale image
            _, mask = cv2.threshold(gray, 255 - tolerance, 255, cv2.THRESH_BINARY)

            # Invert the mask
            mask_inv = cv2.bitwise_not(mask)

            # Split the image into color channels
            b, g, r = cv2.split(image)

            # Create an alpha channel using the inverted mask
            alpha = np.where(mask_inv > 0, 255, 0).astype(np.uint8)

            # Merge the color channels and the alpha channel
            result = cv2.merge((b, g, r, alpha))

            # Construct the output file path
            output_file_path = os.path.join(output_folder_path, filename)

            # Save the modified image in PNG format
            # cv2.imwrite(output_file_path, result)
            cv2.imwrite(output_file_path, result, [cv2.IMWRITE_PNG_COMPRESSION, 4])



print('White color removal with transparency completed.')
