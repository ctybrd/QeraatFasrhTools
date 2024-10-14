from PIL import Image
import os

# Define input and output folders
input_folder = r'D:\temp\Modified'
output_folder = r'D:\temp\small'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Target width and bit depth
target_width = 1296

# Iterate through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.png'):  # Process only PNG files
        input_image_path = os.path.join(input_folder, filename)
        output_image_path = os.path.join(output_folder, filename)

        # Open the image
        with Image.open(input_image_path) as img:
            # Calculate new height to maintain aspect ratio
            width_percent = (target_width / float(img.size[0]))
            new_height = int((float(img.size[1]) * float(width_percent)))

            # Resize the image while keeping aspect ratio
            resized_image = img.resize((target_width, new_height), Image.LANCZOS)

            # Convert to 8-bit (palette-based) and preserve transparency
            converted_image = resized_image.convert('P', palette=Image.ADAPTIVE, colors=256)

            # Save the image with optimization and reduced bit depth
            converted_image.save(output_image_path, optimize=True)

print("Images resized to 1296 width, aspect ratio maintained, and bit depth reduced to 8.")
