from PIL import Image, ImageDraw
import matplotlib.pyplot as plt


class ImageCoordinateSelector:
    def __init__(self, image_path):
        self.image_path = image_path
        self.coordinates_list = []

        # Open the image
        self.image = Image.open(image_path)

        # Create an image draw object
        self.draw = ImageDraw.Draw(self.image)

        # Connect mouse event handler
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(self.image)
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.on_click)

        # Display the image
        plt.show()

    def on_click(self, event):
        # Get the coordinates of the click
        x, y = int(event.xdata), int(event.ydata)

        # Mark the clicked point on the image
        self.draw.point((x, y), fill=(255, 0, 0))  # Mark in red

        # Add the coordinates to the list
        self.coordinates_list.append((x, y))

        # Update the display
        plt.imshow(self.image)
        plt.draw()

    def close_image(self):
        # Close the image window
        plt.close()


def change_black_to_green_in_lines(image_path, output_path, coordinates_list):
    # Open the image
    image = Image.open(image_path)

    # Set the color you want to use for replacing black color (green in RGB)
    replacement_color = (153, 0, 153)

    # Process each set of coordinates
    for coordinates in coordinates_list:
        # Loop through each pair of consecutive coordinates to draw lines
        for i in range(len(coordinates) - 1):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[i + 1]

            # Bresenham's line algorithm to get all pixels along the line
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            sx = 1 if x1 < x2 else -1
            sy = 1 if y1 < y2 else -1
            err = dx - dy

            while x1 != x2 or y1 != y2:
                # Check if the pixel is within the image bounds
                if 0 <= x1 < image.width and 0 <= y1 < image.height:
                    # Check if the current pixel is black
                    if image.getpixel((x1, y1)) == (0, 0, 0):
                        # Change black pixel to green
                        image.putpixel((x1, y1), replacement_color)

                e2 = 2 * err
                if e2 > -dy:
                    err -= dy
                    x1 += sx
                if e2 < dx:
                    err += dx
                    y1 += sy

    # Save the modified image
    image.save(output_path)
    print("Image saved successfully.")


if __name__ == "__main__":
    image_path = "WarshWawat4.png"
    output_path = "WarshWawat4.png"

    # Create an instance of ImageCoordinateSelector to get user-selected coordinates
    selector = ImageCoordinateSelector(image_path)

    # List to store coordinates for multiple lines
    coordinates_list = []

    while True:
        # Get selected coordinates for the current line
        selector_coordinates = selector.coordinates_list.copy()

        # Check if coordinates were selected
        if selector_coordinates:
            # Append the coordinates to the list
            coordinates_list.append(selector_coordinates)

            # Clear the previous coordinates for the next selection
            selector.coordinates_list.clear()

            # Display the image again for the next selection
            selector.fig, selector.ax = plt.subplots()
            selector.ax.imshow(selector.image)
            selector.cid = selector.fig.canvas.mpl_connect('button_press_event', selector.on_click)
            plt.show()

        else:
            # Close the image window and break the loop
            selector.close_image()
            break

    # print coordinates list
    print(coordinates_list)
    # Process the image using the selected coordinates
    change_black_to_green_in_lines(image_path, output_path, coordinates_list)
