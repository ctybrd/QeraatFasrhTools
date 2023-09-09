import os
from PIL import Image, ImageDraw

# Define input folders and their respective column mappings
input_folders = ["folder1", "folder2", "folder3"]
output_folders = ["output_folder1", "output_folder2", "output_folder3"]

# Define column mappings for 5 columns in each output folder
column_mappings = [
    [(0, 2), (1, 3), (2, 4), (0, 0), (1, 1)],  # Output folder 1: Columns from folders 1, 2, 3, 1, 2
    [(1, 2), (2, 3), (0, 4), (2, 0), (3, 1)],  # Output folder 2: Columns from folders 2, 3, 1, 3, 1
    [(2, 1), (0, 3), (1, 4), (1, 0), (2, 2)]   # Output folder 3: Columns from folders 3, 1, 2, 2, 3
]

# Define column widths for each source folder
column_widths = {
    "folder1": [100, 120, 80, 110, 90],  # Example widths for folder 1 columns
    "folder2": [90, 110, 100, 80, 120],  # Example widths for folder 2 columns
    "folder3": [120, 80, 110, 100, 90]   # Example widths for folder 3 columns
}

# Define output image height (in pixels)
output_image_height = 200  # Adjust as needed

# Define the width of the vertical black line between columns
line_width = 2

# Iterate through output folders and their respective column mappings
for output_folder, column_mapping in zip(output_folders, column_mappings):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through PNG images in the input folders with the same names
    for filename in os.listdir(input_folders[0]):
        if filename.endswith(".png"):
            # Initialize an empty list to store columns from source folders
            columns_to_combine = []

            # Iterate through the column mapping for the current output folder
            for source_folder_index, column_index in column_mapping:
                source_folder = input_folders[source_folder_index]
                current_column_widths = column_widths[source_folder]

                # Open the source image and split it into columns based on widths
                source_image_path = os.path.join(source_folder, filename)
                source_img = Image.open(source_image_path)
                column_ranges = [(sum(current_column_widths[:j]), sum(current_column_widths[:j + 1])) for j in range(len(current_column_widths))]
                column = source_img.crop((column_ranges[column_index][0], 0, column_ranges[column_index][1], source_img.height))
                columns_to_combine.append(column)

            # Ensure that we have exactly 5 columns
            if len(columns_to_combine) != 5:
                print(f"Warning: The number of selected columns is not 5 for {output_folder}. Skipping {filename}.")
                continue

            # Calculate the total width of the selected columns and the width of the black lines
            total_width = sum(column.width for column in columns_to_combine) + (len(columns_to_combine) - 1) * line_width

            # Create a new image by combining the selected columns with black lines
            new_img = Image.new("RGBA", (total_width, output_image_height), (0, 0, 0, 255))
            x_offset = 0
            for column in columns_to_combine:
                new_img.paste(column, (x_offset, 0))
                x_offset += column.width + line_width

            # Save the new image in the output folder with the same name
            output_image_path = os.path.join(output_folder, filename)
            new_img.save(output_image_path)

print("Image rearrangement and resizing completed for all output folders.")
