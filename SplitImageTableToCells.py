import cv2
import os
import numpy as np

def split_table_into_cells(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to convert the image to binary
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours in the image
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours from top to bottom
    contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[1])

    # Calculate the average height of the contours
    avg_height = np.mean([cv2.boundingRect(ctr)[3] for ctr in contours])

    # Group contours into rows
    row_contours = []
    current_row = []
    for contour in contours:
        _, y, _, h = cv2.boundingRect(contour)
        if len(current_row) == 0:
            current_row.append(contour)
        elif y - cv2.boundingRect(current_row[-1])[1] <= avg_height / 2:
            current_row.append(contour)
        else:
            row_contours.append(current_row)
            current_row = [contour]
    row_contours.append(current_row)

    # Sort each row's contours from left to right
    for row in row_contours:
        row.sort(key=lambda ctr: cv2.boundingRect(ctr)[0])

    # Create the output folder if it doesn't exist
    output_folder = "d:/temp/"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through the rows and columns
    for row_idx, row in enumerate(row_contours):
        for col_idx, contour in enumerate(row):
            # Get the bounding rectangle for each contour
            x, y, w, h = cv2.boundingRect(contour)

            # Crop the cell region from the original image
            cell_image = image[y:y+h, x:x+w]

            # Save the cell image
            cell_filename = f"cell_{row_idx+1}_{col_idx+1}.jpg"
            cell_filepath = os.path.join(output_folder, cell_filename)
            cv2.imwrite(cell_filepath, cell_image)

    print("Cell images extracted successfully.")

# Specify the path to the input image
image_path = "d:/temp/1.jpg"

# Call the function to split the table into cells
split_table_into_cells(image_path)
