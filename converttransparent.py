from PIL import Image

def convert_background_to_transparent(image_path):
    # Open the image using Pillow
    image = Image.open(image_path)

    # Convert the image to RGBA if it's not already
    if image.mode != "RGBA":
        image = image.convert("RGBA")

    # Get the image dimensions
    width, height = image.size

    # Iterate over each pixel and convert the background to transparent
    for x in range(width):
        for y in range(height):
            r, g, b, a = image.getpixel((x, y))
            # Set the alpha value to 0 for pixels that match the background color
            if (r, g, b) == (255, 255, 255):  # Change this RGB value to match your background color
                image.putpixel((x, y), (r, g, b, 0))

    # Save the image with transparent background
    image.save("transparent_image.png")

# Specify the path to your image
image_path = "path/to/your/image.png"

# Call the function to convert the background to transparent
convert_background_to_transparent(image_path)
