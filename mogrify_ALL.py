import os
import subprocess
import shutil

def process_folder(folder):
    # Change the directory to the target folder
    os.chdir(folder)
    
    # Convert all .png files to .png8 using mogrify
    subprocess.run(['magick', 'mogrify', '-format', 'png8', '*.png'])
    
    # Delete all .png files
    for file in os.listdir(folder):
        if file.endswith('.png'):
            os.remove(file)
    
    # Rename all .png8 files to .png
    for file in os.listdir(folder):
        if file.endswith('.png8'):
            os.rename(file, file[:-4] + 'png')

def copy_folder(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)  # Remove the destination folder if it exists
    shutil.copytree(src, dest)  # Copy the source folder to the destination

# List of folders to process
folders = [
    "F:/Qeraat/NewSides/side",
    "F:/Qeraat/NewSides/side1",
    "F:/Qeraat/NewSides/side2"
]

# List of destination folders
destinations = [
    "F:/Qeraat/Wursha_QuranHolder/src/assets/edition",
    "F:/Qeraat/Wursha_QuranHolder/www/assets/edition",
    "F:/Qeraat/Wursha_QuranHolder_Editions/editions/shmrly/src/assets/edition"
]

# Process each folder
for folder in folders:
    process_folder(folder)

# Copy each processed folder to the three destinations
for folder in folders:
    for dest in destinations:
        dest_path = os.path.join(dest, os.path.basename(folder))
        copy_folder(folder, dest_path)

print("Processing and copying complete.")
