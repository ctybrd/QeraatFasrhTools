from PIL import Image, ImageDraw
import matplotlib.pyplot as plt


class ImageCoordinateSelector:
    def __init__(self, image_path):
        self.image_path = image_path
        self.coordinates = []

        # Open the image
        self.image = Image.open(image_path)

        # Create an image draw object
        self.draw = ImageDraw.Draw(self.image)

        # Connect mouse event handler
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(self.image)
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)

        # Display the image
        plt.show()

    def on_click(self, event):
        # Get the coordinates of the click
        x, y = int(event.xdata), int(event.ydata)

        # Mark the clicked point on the image
        self.draw.point((x, y), fill=(255, 0, 0))  # Mark in red

        # Add the coordinates to the list
        self.coordinates.append((x, y))

        # Update the display
        plt.imshow(self.image)
        plt.draw()

        # Check if two points are selected
        if len(self.coordinates) == 2:
            # Disconnect the event handler after two points are selected
            self.fig.canvas.mpl_disconnect(self.fig)

            # Close the image
            plt.close()

    def get_selected_coordinates(self):
        # Ensure exactly two coordinates are selected
        if len(self.coordinates) == 2:
            # Sort the coordinates to ensure the correct order
            x1, y1 = min(self.coordinates[0][0], self.coordinates[1][0]), min(self.coordinates[0][1],
                                                                              self.coordinates[1][1])
            x2, y2 = max(self.coordinates[0][0], self.coordinates[1][0]), max(self.coordinates[0][1],
                                                                              self.coordinates[1][1])

            return (x1, y1), (x2, y2)
        else:
            raise ValueError("Please select two points on the image.")


def change_black_to_blue_in_rectangular(image_path, output_path, coordinates_list):
    # Open the image
    image = Image.open(image_path)

    replacement_color = (153, 0, 153)

    # Process each set of coordinates
    for coordinates in coordinates_list:
        # Create an image draw object for each set of coordinates
        draw = ImageDraw.Draw(image)

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
                    # Replace black color with blue color
                    draw.point((x, y), fill=replacement_color)

    # Save the modified image
    image.save(output_path)
    print("Image saved successfully.")


if __name__ == "__main__":
    image_path = "WarshEbdal499.png"
    output_path = "WarshWawat499.png"

    # List to store coordinates for multiple rectangular regions
    coordinates_list = []

    while True:
        # Create an instance of ImageCoordinateSelector to get user-selected coordinates
        selector = ImageCoordinateSelector(image_path)

        # Get selected coordinates for the current rectangular region
        selector_coordinates = selector.coordinates.copy()

        # Check if coordinates were selected
        if selector_coordinates:
            # Append the coordinates to the list
            coordinates_list.append(selector_coordinates)

            # Clear the previous coordinates for the next selection
            selector.coordinates.clear()

        # Close the image window
        selector.fig.canvas.mpl_disconnect(selector.fig)
        plt.close()

        # Ask if the user wants to select another rectangular region
        another_region = input("Do you want to select another rectangular region? (y/n): ")
        if another_region.lower() != 'y':
            break

    # print coordinates list
    print(coordinates_list)
    # Process the image using the selected coordinates
    change_black_to_blue_in_rectangular(image_path, output_path, coordinates_list)
