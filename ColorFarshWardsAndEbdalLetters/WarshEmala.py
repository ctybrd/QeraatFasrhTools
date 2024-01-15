from PIL import Image, ImageDraw
import queue
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

        # Check if two points are selected
        if len(self.coordinates_list) == 2:
            # Disconnect the event handler after two points are selected
            self.fig.canvas.mpl_disconnect(self.cid)

    def close_image(self):
        # Close the image window
        plt.close()


def flood_fill(image, x, y, replacement_color, target_color):
    width, height = image.size
    pixels = image.load()

    if pixels[x, y] == target_color:
        q = queue.Queue()
        q.put((x, y))

        while not q.empty():
            current_x, current_y = q.get()

            if (
                0 <= current_x < width
                and 0 <= current_y < height
                and pixels[current_x, current_y] == target_color
            ):
                pixels[current_x, current_y] = replacement_color
                q.put((current_x + 1, current_y))
                q.put((current_x - 1, current_y))
                q.put((current_x, current_y + 1))
                q.put((current_x, current_y - 1))


def change_black_to_blue_in_rectangular(image_path, output_path, coordinates_list):
    # Open the image
    image = Image.open(image_path)

    # Set the color you want to use for replacing black color (blue in RGB)
    replacement_color = (65, 105, 225)

    # Process each set of coordinates
    for coordinates in coordinates_list:
        # Extract the x and y coordinates
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

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
                    # Perform flood fill operation to change all connected black pixels to blue
                    flood_fill(image, x, y, replacement_color, (0, 0, 0))

    # Save the modified image
    image.save(output_path)
    print("Image saved successfully.")


if __name__ == "__main__":
    image_path = "WarshWawat4.png"
    output_path = "WarshEmala4.png"

    # Create an instance of ImageCoordinateSelector to get user-selected coordinates
    selector = ImageCoordinateSelector(image_path)

    # List to store coordinates for multiple rectangular regions
    coordinates_list = []

    while True:
        # Get selected coordinates for the current rectangular region
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

    # Process the image using the selected coordinates
    change_black_to_blue_in_rectangular(image_path, output_path, coordinates_list)
