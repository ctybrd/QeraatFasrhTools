import fitz  # PyMuPDF

# Function to create a circle annotation with the specified properties
def create_circle(page, center, radius, color):
    # Create a new circle annotation
    circle = page.draw_circle(center, radius)
    
    # Set the circle annotation's appearance properties
    # circle.set_colors(stroke=color, fill=color)  # Set both stroke and fill color
    
    # Remove the old line annotation
    # page.delete_annotation(circle)
    
    return circle

# Open the PDF file
pdf_file = "E:\Qeraat\AbuAmro-Shamarly-Shalaby.pdf"
pdf_document = fitz.open(pdf_file)

# Loop through pages
for page_num in range(pdf_document.page_count):
    page = pdf_document.load_page(page_num)
    
    # Iterate over page annotations (comments)
    for annotation in page.annots():
        if annotation.type[0] == 3:  # Check if it's a line annotation
            # Get the bounding rectangle
            rect = annotation.rect
            
            # Calculate the center of the rectangle
            x_center = (rect.x0 + rect.x1) / 2
            y_center = (rect.y0 + rect.y1) / 2
            radius = 10  # Adjust the circle radius as needed

            # Create a new circle annotation with cyan color
            create_circle(page, (x_center, y_center), radius, (0.0, 1.0, 1.0))

            # Remove the old line annotation
            # page.delete_annotation(annotation)

# Save the modified PDF
pdf_document.save("output.pdf")

# Close the PDF document
pdf_document.close()
