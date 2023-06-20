from PIL import Image
import os

# Path to the directory containing the original images
original_images_dir = "E:\Qeraat\ShmrlySides\side"

# Path to the directory containing the side column images
side_column_images_dir = "E:\Qeraat\ShmrlySides\SideW"

# Path to the output directory for the combined images
output_dir = "E:\Qeraat\ShmrlySides\SideNew"

# Get a list of file names from the original images directory
original_images_files = os.listdir(original_images_dir)

# Iterate through each original image
for image_file in original_images_files:
    # Load the original image
    original_image_path = os.path.join(original_images_dir, image_file)
    original_image = Image.open(original_image_path).convert("RGBA")

    # Get the corresponding side column image
    side_column_image_file = image_file  
    # .replace(".png", ".jpg")
    side_column_image_path = os.path.join(side_column_images_dir, side_column_image_file)
    side_column_image = Image.open(side_column_image_path).convert("RGBA")

    # Check if both images were successfully loaded
    if original_image is not None and side_column_image is not None:
        # Resize the side column image to one-sixth of the width of the original image
        side_width = original_image.width // 6
        side_height = original_image.height
        side_column_image = side_column_image.resize((side_width, side_height))
        original_width =(original_image.width*5) // 6

        original_image = original_image.resize((original_width,side_height))
        
        # Create a new image with the combined width
        combined_width = original_image.width + side_column_image.width
        combined_height = original_image.height
        combined_image = Image.new("RGBA", (combined_width, combined_height))

        # Paste the original image on the left side of the combined image
        combined_image.paste(original_image, (0, 0))

        # Paste the resized side column image on the right side of the combined image
        combined_image.paste(side_column_image, (original_image.width, 0))

        # Convert the combined image to have a transparent background
        combined_image = combined_image.convert("RGBA")

        # Create a new image with transparent background
        transparent_image = Image.new("RGBA", combined_image.size, (0, 0, 0, 0))

        # Paste the combined image onto the transparent image
        transparent_image.paste(combined_image, (0, 0), mask=combined_image)

        # Save the transparent image to the output directory
        output_image_path = os.path.join(output_dir, image_file)
        transparent_image.save(output_image_path)
    else:
        print(f"Failed to load images for {image_file}")

print("Image combination and transparent background conversion completed.")
