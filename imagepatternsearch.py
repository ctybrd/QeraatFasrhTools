import cv2
import numpy as np

# Step 1: Load images
image_list = ['E:/Qeraat/QeraatFasrhTools_Data/waqfmarks/73.png','E:/Qeraat/QeraatFasrhTools_Data/waqfmarks/75.png']  # Provide paths or data for your images

# Step 2: Define a template or pattern image
template = cv2.imread('E:/Qeraat/QeraatFasrhTools_Data/waqfmarks/object1.png', 0)  # Replace 'pattern.jpg' with your pattern image

# Step 3: Loop through each image
for img_path in image_list:
    # Load the image
    img = cv2.imread(img_path, 0)

    # Step 4: Match the pattern in the image
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    # Set a threshold to consider a match
    threshold = 0.8
    loc = np.where(res >= threshold)

    # Step 5: Mark the matches
    for pt in zip(*loc[::-1]):
        # Draw a rectangle around the matched area
        cv2.rectangle(img, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), 255, 2)

    # Display or save the marked image
    cv2.imshow('Marked Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
