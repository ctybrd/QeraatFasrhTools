import os

folder_path = 'E:/JS_Course'  # Replace with the actual folder path

# List all files in the folder
files = os.listdir(folder_path)

for file_name in files:
    if '@' in file_name:
        # Extract the number from the file name
        number_start = file_name.index('@') + 1
        number_end = number_start
        while number_end < len(file_name) and file_name[number_end].isdigit():
            number_end += 1

        if number_start < number_end:
            number = file_name[number_start:number_end]

            # Create the new file name with the number at the beginning
            new_file_name = f"{number.zfill(2)} {number.zfill(2)} {file_name}"

            # Rename the file
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_file_name)

            os.rename(old_path, new_path)
            print(f"Renamed {file_name} to {new_file_name}")
