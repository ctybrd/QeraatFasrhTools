from PIL import Image
import os
import subprocess
from sklearn.cluster import KMeans
import numpy as np

# Function to quantize the image (reduce the number of colors)
def quantize_image(image_path, n_colors=16):
    image = Image.open(image_path)
    image = image.convert('RGB')  # Ensure the image is in RGB mode
    
    # Convert the image into a numpy array
    img_data = np.array(image)
    pixels = img_data.reshape((-1, 3))
    
    # Apply KMeans to reduce the number of colors
    kmeans = KMeans(n_clusters=n_colors, random_state=42)
    kmeans.fit(pixels)
    new_colors = kmeans.cluster_centers_[kmeans.labels_]
    
    # Recreate the image with the new color palette
    quantized_img_data = new_colors.reshape(img_data.shape).astype('uint8')
    quantized_image = Image.fromarray(quantized_img_data)

    # Save the quantized image as PPM (needed for Potrace to keep color data)
    ppm_path = image_path.replace('.png', '.ppm')
    quantized_image.save(ppm_path, 'PPM')

    return ppm_path

# Function to convert PPM to SVG using Potrace
def convert_ppm_to_svg(ppm_paths):
    svg_paths = []
    for ppm_path in ppm_paths:
        svg_path = ppm_path.replace('.ppm', '.svg')
        subprocess.run(['potrace', ppm_path, '-s', '-o', svg_path])
        svg_paths.append(svg_path)
    return svg_paths

# Main process
input_folder = 'e:/temp'
output_folder = 'e:/temp'
os.makedirs(output_folder, exist_ok=True)

# List all PNG files in the input folder
image_paths = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.png')]

# Quantize and convert PNG to PPM
ppm_paths = []
for image_path in image_paths:
    ppm_path = quantize_image(image_path, n_colors=16)
    ppm_paths.append(ppm_path)

# Convert PPM to SVG
svg_paths = convert_ppm_to_svg(ppm_paths)

print("SVG files generated:", svg_paths)
