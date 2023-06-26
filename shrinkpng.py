from PIL import Image
import os

# Directory containing the PNG images
directory = 'e:/SideNew/'

# Create a new directory to store compressed images
compressed_directory = 'e:/SideNew_Less/'
os.makedirs(compressed_directory, exist_ok=True)

# Iterate through each PNG image in the directory
for filename in os.listdir(directory):
    if filename.endswith('.png'):
        # Open the image using Pillow
        image_path = os.path.join(directory, filename)
        image = Image.open(image_path)

        # Convert the image to PNG format and apply compression settings
        image = image.convert('RGBA')  # Ensure transparency is preserved
        image.save(os.path.join(compressed_directory, filename), optimize=True, pngquant=100)

        # Close the image file
        image.close()
