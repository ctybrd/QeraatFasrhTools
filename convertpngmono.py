from PIL import Image
import os

def convert_to_monochrome(file_path):
    # Open the image
    image = Image.open(file_path)

    # Convert to monochrome
    image = image.convert('L')

    # Reduce the file size
    image.save(file_path, optimize=True, quality=95)

directory = 'E:/Qeraat/ShmrlySides/SideNew_Mono/'  # Replace with the directory containing your PNG files

for filename in os.listdir(directory):
    if filename.endswith(".png"):
        file_path = os.path.join(directory, filename)
        convert_to_monochrome(file_path)
