import cv2
import numpy as np
import os
import sqlite3

# Function to get the average color of a region in BGR format
def get_average_color(image, contour):
    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.drawContours(mask, [contour], -1, 255, -1)
    mean = cv2.mean(image, mask=mask)[:3]
    return mean

# Function to detect colored text and insert positions into the database
def process_image_and_insert_to_db(image_path, db_path, qaree, style, circle):
    # Read the image with alpha channel
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if image is None:
        print(f"Unable to read image: {image_path}")
        return

    # Check if the image has an alpha channel (transparency)
    if image.shape[2] == 4:
        # Separate the alpha channel
        bgr_image = image[:, :, :3]
        alpha_channel = image[:, :, 3]
    else:
        bgr_image = image

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

    # Define color range for detection (example range for red color)
    lower_color = np.array([0, 50, 50])
    upper_color = np.array([10, 255, 255])

    # Create a mask for the colored regions
    mask = cv2.inRange(hsv_image, lower_color, upper_color)

    # Optionally, use the alpha channel to refine the mask if needed
    if image.shape[2] == 4:
        mask = cv2.bitwise_and(mask, mask, mask=alpha_channel)

    # Find contours of the masked regions
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for contour in contours:
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Calculate ratios
        x_ratio = x / image.shape[1]
        y_ratio = y / image.shape[0]
        width_ratio = w / image.shape[1]

        # Get the average color of the contour
        avg_color_bgr = get_average_color(bgr_image, contour)
        avg_color_rgb = (avg_color_bgr[2], avg_color_bgr[1], avg_color_bgr[0])  # Convert BGR to RGB

        # Insert data into the database
        cursor.execute("""
            INSERT INTO madina (qaree, page_number, color, x, y, width, style, circle)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (qaree, page_number, str(avg_color_rgb), x_ratio, y_ratio, width_ratio, style, circle))

    # Commit and close the connection
    conn.commit()
    conn.close()

# Path to the folder containing images
input_folder = 'D:/pages'
db_path = 'D:/Qeraat/farsh_v9.db'

# Process each image in the folder
for filename in os.listdir(input_folder):
    if filename.endswith('.png'):  # Adjusted to process only PNG files
        input_path = os.path.join(input_folder, filename)
        page_number = os.path.splitext(filename)[0]  # Use file name (without extension) as page_number
        qaree = 'A'  # Replace with actual qaree
        style = ''  # Replace with actual style
        circle = ''  # Replace with actual circle
        process_image_and_insert_to_db(input_path, db_path, qaree, style, circle)
