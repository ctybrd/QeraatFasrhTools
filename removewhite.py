import os
import cv2
import numpy as np

folder_path = r'E:\Qeraat\ShmrlySides\SideI'
tolerance = 30  # Adjust this value based on your needs

# Create a new folder to save the modified images
output_folder_path = os.path.join(folder_path, 'Modified')
os.makedirs(output_folder_path, exist_ok=True)

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
        cv2.imwrite(output_file_path, result)

print('White color removal with transparency completed.')
