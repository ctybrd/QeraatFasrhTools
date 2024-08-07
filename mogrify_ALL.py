import os
import subprocess
import shutil

def process_folder(folder):
    # Convert all .png files to .png8 using mogrify
    subprocess.run(['magick', 'mogrify', '-format', 'png8', os.path.join(folder, '*.png')])
    
    # Delete all .png files
    for file in os.listdir(folder):
        if file.endswith('.png') and not file.endswith('.png8'):
            os.remove(os.path.join(folder, file))
    
    # Rename all .png8 files to .png
    for file in os.listdir(folder):
        if file.endswith('.png8'):
            os.rename(os.path.join(folder, file), os.path.join(folder, file[:-4] + 'png'))

def copy_folder(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)  # Remove the destination folder if it exists
    shutil.copytree(src, dest)  # Copy the source folder to the destination

# Root directory to make script drive-independent
script_path = os.path.abspath(__file__)
drive, _ = os.path.splitdrive(script_path)
drive = drive +'/'


# List of folders to process
folders = [
    os.path.join(drive, "Qeraat/NewSides/side"),
    os.path.join(drive, "Qeraat/NewSides/side1"),
    os.path.join(drive, "Qeraat/NewSides/side2")
]

# List of destination folders
destinations = [
    os.path.join(drive, "Qeraat/Wursha_QuranHolder/src/assets/edition"),
    os.path.join(drive, "Qeraat/Wursha_QuranHolder/www/assets/edition"),
    os.path.join(drive, "Qeraat/Wursha_QuranHolder_Editions/editions/shmrly/src/assets/edition")
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
