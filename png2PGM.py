from PIL import Image
import os
import subprocess

# Function to convert PNG to PGM
def convert_png_to_pgm(image_paths):
    pgm_paths = []
    for image_path in image_paths:
        image = Image.open(image_path).convert('L')  # Convert to grayscale
        pgm_path = image_path.replace('.png', '.pgm')
        image.save(pgm_path)
        pgm_paths.append(pgm_path)
    return pgm_paths

# Function to convert PGM to SVG using Potrace
def convert_pgm_to_svg(pgm_paths):
    svg_paths = []
    for pgm_path in pgm_paths:
        svg_path = pgm_path.replace('.pgm', '.svg')
        subprocess.run(['potrace', pgm_path, '-s', '-o', svg_path])
        svg_paths.append(svg_path)
    return svg_paths

# Main process
input_folder = 'F:/QaloonColored'
output_folder = 'F:/QaloonColored_out'
os.makedirs(output_folder, exist_ok=True)

# List all PNG files in the input folder
image_paths = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.png')]

# Convert PNG to PGM
pgm_paths = convert_png_to_pgm(image_paths)

# Convert PGM to SVG
svg_paths = convert_pgm_to_svg(pgm_paths)

print("SVG files generated:", svg_paths)
