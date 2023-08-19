from PIL import Image, ImageOps, ImageDraw
import os

# Define the paths for the source folders and the destination folder
folder_paths = [
    r'E:\Qeraat\QeraatFasrhTools_Data\ShmrlySides\SideW',
    r'E:\Qeraat\QeraatFasrhTools_Data\ShmrlySides\SideI',
    r'E:\Qeraat\QeraatFasrhTools_Data\ShmrlySides\SideSela'
]
destination_folder = r'E:\Qeraat\QeraatFasrhTools_Data\ShmrlySides\Side1'

# Ensure the destination folder exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Iterate through the range of images (1.png to 522.png)
for i in range(1, 523):
    image_paths = [os.path.join(folder, f'{i}.png') for folder in folder_paths]

    # Open the images and resize their widths to 300 pixels
    images = [Image.open(image_path).resize((300, 2407), Image.LANCZOS) for image_path in image_paths]

    # Create a new blank image with the desired width and height
    total_width = sum(image.width for image in images) + (len(images) - 1)  # Add space for vertical lines
    concatenated_image = Image.new('RGBA', (total_width, 2407), (0, 0, 0, 0))

    # Paste each image onto the concatenated image with vertical lines
    x_offset = 0
    draw = ImageDraw.Draw(concatenated_image)
    for image in images:
        concatenated_image.paste(image, (x_offset, 0))
        x_offset += image.width
        if x_offset < total_width:
            draw.line([(x_offset, 0), (x_offset, 2406)], fill=(0, 0, 0), width=1)
            x_offset += 1  # Space for the line

    # Save the concatenated image
    concatenated_image_path = os.path.join(destination_folder, f'{i}.png')
    concatenated_image.save(concatenated_image_path)

print("Concatenation with vertical lines completed.")
