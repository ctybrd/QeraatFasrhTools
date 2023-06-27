import cv2
import numpy as np

def crop_text_areas(image_path):
    # Load and preprocess the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply edge detection to find contours
    edged = cv2.Canny(blurred, 30, 150)

    # Find contours in the image
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over the contours and filter out small ones
    min_contour_area = 200
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

    # Crop and save each text area as a separate image
    for i, contour in enumerate(filtered_contours):
        x, y, w, h = cv2.boundingRect(contour)
        text_area = image[y:y+h, x:x+w]
        cv2.imwrite(f"d:/temp/text_area_{i}.jpg", text_area)

# Run the program for a specific image
image_path = "d:/temp/2.jpg"
crop_text_areas(image_path)
