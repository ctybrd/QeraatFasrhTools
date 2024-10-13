from PIL import Image
import os
import subprocess
from sklearn.cluster import KMeans
import numpy as np

# Function to quantize the image (reduce the number of colors)
def quantize_image(image_path, output_folder, n_colors=16):
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

    # Save the quantized image as PPM in the output folder (needed for Inkscape to keep color data)
    base_filename = os.path.basename(image_path).replace('.png', '.ppm')
    ppm_path = os.path.join(output_folder, base_filename)
    quantized_image.save(ppm_path, 'PPM')

    return ppm_path

# Function to optimize SVG using SVGO
def optimize_svg_with_svgo(svg_path):
    try:
        # Call SVGO to optimize the SVG file
        subprocess.run(['svgo', svg_path, '-o', svg_path], check=True)
        print(f"Optimized {svg_path} with SVGO.")
    except FileNotFoundError:
        print("SVGO is not installed. Skipping optimization.")
    except subprocess.CalledProcessError as e:
        print(f"Error optimizing {svg_path} with SVGO: {e}")

# Function to convert PPM to SVG using Inkscape
def convert_ppm_to_svg(ppm_paths, output_folder):
    svg_paths = []
    for ppm_path in ppm_paths:
        base_filename = os.path.basename(ppm_path).replace('.ppm', '.svg')
        svg_path = os.path.join(output_folder, base_filename)
        
        # Run Inkscape and capture the output to log errors if any
        try:
            result = subprocess.run([
                'inkscape', ppm_path, 
                '--export-filename', svg_path, 
                '--export-dpi=300'  # Export at 300 DPI for clarity without excessive resolution
            ], capture_output=True, text=True, check=True)
            
            # Print Inkscape output for debugging
            print(result.stdout)
            print(f"SVG created: {svg_path}")

            # Optimize the SVG using SVGO if available
            optimize_svg_with_svgo(svg_path)
            svg_paths.append(svg_path)

        except subprocess.CalledProcessError as e:
            print(f"Error generating {svg_path} with Inkscape: {e.stderr}")
        
    return svg_paths

# Main process
input_folder = 'F:/QaloonColored'
output_folder = 'F:/QaloonColored_SVG'
os.makedirs(output_folder, exist_ok=True)

# List all PNG files in the input folder
image_paths = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.png')]

# Quantize and convert PNG to PPM
ppm_paths = []
for image_path in image_paths:
    ppm_path = quantize_image(image_path, output_folder, n_colors=16)
    ppm_paths.append(ppm_path)

# Convert PPM to SVG and optimize with SVGO
svg_paths = convert_ppm_to_svg(ppm_paths, output_folder)

print("Optimized SVG files generated:", svg_paths)
