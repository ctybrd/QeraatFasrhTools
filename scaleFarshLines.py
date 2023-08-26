from pdfrw import PdfReader, PdfWriter

# Read the original FDF file
original_fdf = PdfReader('E:\\Qeraat\\Warsh.pdf')

# Define the ratio by which you want to modify the coordinates
x_ratio = 1.25  # Increase x coordinates by 50%
y_ratio = 1.39  # Increase y coordinates by 50%

# Modify the coordinates in the FDF data
modified_fdf = original_fdf
for page in modified_fdf.pages:
    if '/Annots' in page and page['/Annots']:
        for annot in page['/Annots']:
            if isinstance(annot, dict) and '/Rect' in annot and isinstance(annot['/Rect'], list):
                rect_array = annot['/Rect']
                for i in range(len(rect_array)):
                    if i % 2 == 0:
                        rect_array[i] = int(float(rect_array[i]) * x_ratio)  # Update x coordinate
                    else:
                        rect_array[i] = int(float(rect_array[i]) * y_ratio)  # Update y coordinate

# Write modified FDF data to a new PDF file
PdfWriter().write('E:\\Qeraat\\Warsh1.pdf', modified_fdf)
