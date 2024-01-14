from PIL import Image, ImageDraw


def change_black_to_blue_in_rectangular(image_path, output_path, coord1, coord2):
    # Open the image
    image = Image.open(image_path)

    # Create an image draw object
    draw = ImageDraw.Draw(image)

    # Set the color you want to use for replacing black color (blue in RGB)
    replacement_color = (0, 0, 255)

    # Ensure that two coordinates are provided
    if len(coord1) == 2 and len(coord2) == 2:
        # Extract the x and y coordinates
        x1, y1 = coord1
        x2, y2 = coord2

        # Sort the coordinates to ensure the correct order
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)

        # Loop through each pixel in the specified rectangular region
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                # Get the RGB values of the current pixel
                current_color = image.getpixel((x, y))

                # Check if the current pixel is black
                if current_color == (0, 0, 0):
                    # Replace black color with blue color
                    draw.point((x, y), fill=replacement_color)

        # Save the modified image
        image.save(output_path)
        print("Image saved successfully.")
    else:
        print("Please provide two sets of coordinates for the rectangular region.")


if __name__ == "__main__":
    image_path = "4.png"  # Assuming the image is in the same directory as your script
    output_path = "blue_rectangular_quran_page_4.png"

    # Define the coordinates for the rectangular region
    coord1 = (423, 179)
    coord2 = (471, 241)

    change_black_to_blue_in_rectangular(image_path, output_path, coord1, coord2)
