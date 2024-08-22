import os

directory = 'D:/QPages1'  # Replace with the path to your directory

# Loop through the range of numbers you want to rename
for i in range(2, 604):  # From 2 to 603 inclusive
    original_filename = f'{i}.png'
    new_filename = f'{i-1}.png'

    original_path = os.path.join(directory, original_filename)
    new_path = os.path.join(directory, new_filename)

    # Check if the original file exists before renaming
    if os.path.exists(original_path):
        os.rename(original_path, new_path)
    else:
        print(f"File {original_filename} does not exist and will be skipped.")
