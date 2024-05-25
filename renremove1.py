import os
import glob

# Define the base directory
base_dir = r'F:\Qeraat\NewSides'

# Use glob to find all files matching the pattern *1.png in the base directory and subdirectories
for file_path in glob.iglob(os.path.join(base_dir, '**', '*1.png'), recursive=True):
    # Get the directory name and file name
    dir_name = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    
    # Define the new file name by removing the '1' before '.png'
    new_file_name = file_name.replace('1.png', '.png')
    
    # Create the full new file path
    new_file_path = os.path.join(dir_name, new_file_name)
    
    # Rename the file
    os.rename(file_path, new_file_path)
    
    # Print the old and new file paths for verification
    print(f'Renamed: {file_path} -> {new_file_path}')
