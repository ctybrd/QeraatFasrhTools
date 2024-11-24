import os

directory = 'D:/TEMP'  # Replace with the path to your directory

# Loop through the range of numbers you want to rename
for i in range(1, 524):  # From 1 to 522 inclusive
    original_filename = f'{i}.png'  # Leading zeros format (e.g., 001, 002, etc.)
    new_filename = f'{i-2}.png'  # Remove leading zeros

    original_path = os.path.join(directory, original_filename)
    new_path = os.path.join(directory, new_filename)

    # Check if the original file exists before renaming
    if os.path.exists(original_path):
        os.rename(original_path, new_path)
        print(f"Renamed {original_filename} to {new_filename}")
    else:
        print(f"File {original_filename} does not exist and will be skipped.")
