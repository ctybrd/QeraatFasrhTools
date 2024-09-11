import os
import re

# Define the folder path and the file pattern
folder_path = 'D:/Qeraat/QeraatFasrhTools_Data/Ten_Readings/json'
file_pattern = re.compile(r'_([0-9]+)\.json$')

# Get the list of files in the folder
files = os.listdir(folder_path)

# Extract numbers from filenames
file_numbers = []
for file_name in files:
    match = file_pattern.search(file_name)
    if match:
        file_numbers.append(int(match.group(1)))

# Find the missing numbers in the range 1 to 606
all_numbers = set(range(1, 604))
existing_numbers = set(file_numbers)
missing_numbers = sorted(all_numbers - existing_numbers)

# Print the missing numbers
print("Missing numbers:", missing_numbers)
