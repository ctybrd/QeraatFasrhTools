import json

# Path to the JSON file
file_path = 'E:/Qeraat/QeraatFasrhTools_Data/Ten_Readings/json/Qeraat_303.json'

# Function to extract text from chars
def extract_text_from_chars(chars):
    return ''.join([char['unicode'] for char in chars])

# Read and process the JSON file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

    for item in data:
        word_text = item['word_text']
        print(f"Word: {word_text}")
        
        detail_text = extract_text_from_chars(item['detail_title_chars'])
        print(f"Detail Title: {detail_text}")
        
        for reading in item['quran_ten_word_mp3']:
            reading_order = reading['reading_order']
            file_path = reading['file']
            reading_detail_text = extract_text_from_chars(reading['detail_chars'])
            print(f"Reading Order: {reading_order}")
            print(f"File Path: {file_path}")
            print(f"Reading Detail: {reading_detail_text}")
        print("\n" + "-"*50 + "\n")
