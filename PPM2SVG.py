from PIL import Image
import os
import svgwrite

input_folder = 'F:/QaloonColored_SVG'
output_folder = 'F:/QaloonColored_SVG'

def ppm_to_svg(ppm_file, svg_file):
    # Open PPM file using Pillow
    with Image.open(ppm_file) as img:
        # Create SVG file with the same dimensions
        dwg = svgwrite.Drawing(svg_file, size=(img.width, img.height))
        
        # Convert the image pixels to rectangles or paths here
        # This is a simplistic example; you might want to explore better vectorization techniques.
        
        # Save SVG file
        dwg.save()

# Ensure the output directory exists
os.makedirs(output_folder, exist_ok=True)

# Convert all PPM files in the folder
for filename in os.listdir(input_folder):
    if filename.endswith('.ppm'):
        ppm_file = os.path.join(input_folder, filename)
        svg_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.svg")
        ppm_to_svg(ppm_file, svg_file)

print(f"Conversion complete. SVG files are saved in {output_folder}.")
