import os
import cv2
import numpy as np

def remove_column_and_resize(image_path, column_start, column_end):
    # Read the image
    image = cv2.imread(image_path)

    # Get image width and height
    height, width = image.shape[:2]

    # Create a mask with ones everywhere except the region to remove
    mask = np.ones((height, width), dtype=np.uint8)
    mask[:, column_start:column_end] = 0

    # Apply the mask to remove the column
    image_without_column = cv2.bitwise_and(image, image, mask=mask)

    # Concatenate the remaining parts horizontally
    image_concatenated = np.concatenate((image_without_column[:, :column_start], image_without_column[:, column_end:]), axis=1)

    # Calculate the new width (excluding the removed column)
    net_width = width - (column_end - column_start)

    # Resize the final image to the new width
    resized_image = cv2.resize(image_concatenated, (net_width, height))

    return resized_image

def swap_parts(image, swap_point):
    # Get image width
    width = image.shape[1]

    # Calculate the new position for the swap point
    new_swap_point = swap_point if swap_point < width else width - 1

    # Swap the parts after the swap point
    swapped_image = np.hstack((image[:, new_swap_point:], image[:, :new_swap_point]))

    return swapped_image

def process_images_in_folder(folder_path, column_start, column_end, swap_point):
    # Make sure the output folder exists
    output_folder = os.path.join(folder_path, "output")
    os.makedirs(output_folder, exist_ok=True)

    # Process each image in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            image_path = os.path.join(folder_path, filename)
            resized_image = remove_column_and_resize(image_path, column_start, column_end)

            # Swap the parts and save the processed image in the output folder
            swapped_image = swap_parts(resized_image, swap_point)
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, swapped_image)

if __name__ == "__main__":
    # Specify the folder containing the images
    folder_path = "E:/Qeraat/QeraatFasrhTools_Data/Hamzah_Damrah"

    # Specify the column region to remove
    column_start = 521
    column_end = 769

    # Specify the point where you want to swap the parts
    swap_point = 167

    # Process images in the folder, remove column, and swap parts
    process_images_in_folder(folder_path, column_start, column_end, swap_point)
