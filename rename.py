import os

directory = 'E:\ShmrlySides\SideW'  # Replace with the path to your directory

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.png'):  # Replace '.txt' with the file extension you're working with
        new_filename = filename.lstrip('0')  # Remove leading zeros
        original_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        os.rename(original_path, new_path)