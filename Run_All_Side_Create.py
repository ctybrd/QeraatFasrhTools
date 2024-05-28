import subprocess
import os

def run_script(script_name):
    print(f"Starting {script_name}...")
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    print(f"Completed {script_name}")
    # print(f"Return code: {result.return_code}")
    # if result.return_code != 0:
    #     print(f"Error running {script_name}: {result.stderr}")
    # else:
    #     print(f"Output of {script_name}: {result.stdout}")

# Get the absolute path of the script
script_path = os.path.abspath(__file__)

# Extract the drive letter
drive, _ = os.path.splitdrive(script_path)
drive = drive +'/'
# Define the base paths using the extracted drive letter
scripts_folder = os.path.join(drive, 'Qeraat', 'QeraatFasrhTools')

# Export pdf to slices png files
run_script(os.path.join(scripts_folder, 'Export_pdf_png_ALL.py'))

# Remove white make transparent slices
run_script(os.path.join(scripts_folder, 'removewhite_ALL.py'))

# Concat each 5 slices in one image 
run_script(os.path.join(scripts_folder, 'ConcatImages_ALL.py'))

# Mogrify ALL
run_script(os.path.join(scripts_folder, 'mogrify_ALL.py'))
