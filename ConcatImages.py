from PIL import Image, ImageDraw
import os

# Path to the directory containing the original images
#after merging use imagemagick to reduce size
#magick mogrify -format png8 *.png
original_images_dir = "E:\Qeraat\QeraatFasrhTools_Data\ShmrlySides\side"

# Path to the directory containing the side column images
side_column_images_dir = "E:\Qeraat\QeraatFasrhTools_Data\ShmrlySides\SideSela"

# Path to the output directory for the combined images
output_dir = "E:\Qeraat\QeraatFasrhTools_Data\ShmrlySides\SideNew"

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
    
    # Load the side column image
    side_column_image = Image.open(side_column_image_path).convert("RGBA")

    # Create a new image with transparency
    # side_column_image_with_alpha = Image.new("RGBA", side_column_image.size)

    # # Iterate through each pixel of the side column image
    # for x in range(side_column_image.width):
    #     for y in range(side_column_image.height):
    #         # Get the pixel color at the current position
    #         pixel = side_column_image.getpixel((x, y))
            
    #         # Check if the pixel color is white
    #         if pixel[:3] == (255, 255, 255):
    #             # Set the alpha value to 0 to make it transparent
    #             side_column_image_with_alpha.putpixel((x, y), (0, 0, 0, 0))
    #         else:
    #             # Preserve the original pixel color
    #             side_column_image_with_alpha.putpixel((x, y), pixel)

    # Check if both images were successfully loaded
    if original_image is not None and side_column_image is not None:
        # Resize the original image width to be 6/7 of the original width
        new_width = original_image.width #int(original_image.width * 6 / 7)
        new_height = original_image.height
        resized_original_image = original_image.resize((new_width, new_height))

        # Resize the side column image to be 1/7 of the original image width
        side_width = int(original_image.width / 7)
        side_height = resized_original_image.height
        resized_side_column_image = side_column_image.resize((side_width, side_height))

        # Create a new image with the combined width
        combined_width = resized_original_image.width + resized_side_column_image.width + 6
        combined_height = resized_original_image.height
        combined_image = Image.new("RGBA", (combined_width, combined_height), (0, 0, 0, 0))

        # Paste the resized original image on the left side of the combined image
        combined_image.paste(resized_original_image, (0, 0))

        # Paste the resized side column image on the right side of the combined image
        combined_image.paste(resized_side_column_image, (resized_original_image.width + 3, 0))

        # Draw a vertical black line to the right of the original image
        draw = ImageDraw.Draw(combined_image)
        draw.line([(resized_original_image.width, 0), (resized_original_image.width, combined_height)], fill=(0, 0, 0), width=3)

        # Create the final image with a black line to the right
        final_width = combined_width + 6
        final_height = combined_height
        final_image = Image.new("RGBA", (final_width, final_height), (0, 0, 0, 0))

        # Paste the combined image onto the final image
        final_image.paste(combined_image, (0, 0))

        # Draw a vertical black line to the right of the final image
        draw_final = ImageDraw.Draw(final_image)
        draw_final.line([(combined_width, 0), (combined_width, final_height)], fill=(0, 0, 0), width=3)

        # Save the final image to the output directory
        output_image_path = os.path.join(output_dir, image_file)
        final_image.save(output_image_path)
    else:
        print(f"Failed to load images for {image_file}")

print("Image combination and transparency conversion completed.")
