import os
import json

def extract_text(json_data):
    text = ""
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if isinstance(value, str):
                text += value + " "
            else:
                text += extract_text(value)
    elif isinstance(json_data, list):
        for item in json_data:
            text += extract_text(item)
    return text

folder_path = r'E:/Qeraat/QeraatFasrhTools_Data/Ten_Readings/json'
output_path = r'E:/Qeraat/QeraatFasrhTools_Data/Ten_Readings/output.txt'  # Path to the output text file

# Iterate over files in the folder
with open(output_path, 'w', encoding='utf-8') as output_file:
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    json_data = json.load(file)
                    # Extract all textual data
                    text = extract_text(json_data)
                    output_file.write(text + '\n')

                    # Additional processing for each JSON file can be added here

            except Exception as e:
                print(f"Error processing file {filename}: {e}")
