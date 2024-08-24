import os
import cv2
import numpy as np

folder_path = r'D:/QPages'
output_folder_path = os.path.join(folder_path, 'Modified')
os.makedirs(output_folder_path, exist_ok=True)

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg'):
        file_path = os.path.join(folder_path, filename)

        # Read the image using OpenCV
        image = cv2.imread(file_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Create a mask that isolates grayscale (darker) areas
        # Adjust threshold as needed; this one keeps black and dark grays
        _, mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

        # Use the mask as the alpha channel
        b, g, r = cv2.split(image)
        alpha_channel = mask

        # Merge the BGR channels with the alpha channel
        result = cv2.merge((b, g, r, alpha_channel))

        # Construct the output file path, replacing .jpg with .png
        output_file_path = os.path.join(output_folder_path, filename.replace('.jpg', '.png'))

        # Save the modified image in PNG format with transparency
        cv2.imwrite(output_file_path, result)

print('Retained black and grayscale areas, and converted to PNG with transparency.')
