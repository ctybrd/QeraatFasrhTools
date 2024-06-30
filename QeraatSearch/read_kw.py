import json
import os

# Path to the JSON file
script_path = os.path.abspath(__file__)
drive, _ = os.path.splitdrive(script_path) 
drive = drive +'/'

file_path = os.path.join(drive,'Qeraat/QeraatFasrhTools_Data/Ten_Readings/json/Qeraat_118.json')
def extract_text_from_chars(chars):
    return ''.join([char['unicode'] for char in chars])
def transliterate_number(number):
    mapping = {
        '٠': '0',
        '١': '1',
        '٢': '2',
        '٣': '3',
        '٤': '4',
        '٥': '5',
        '٦': '6',
        '٧': '7',
        '٨': '8',
        '٩': '9',
    }
    return ''.join(mapping.get(char, char) for char in str(number))

# Read and process the JSON file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

    for item in data:
        sub_subject = item['word_text']
        print(f"SUB_SUBJECT: {sub_subject}")
        
        notes = extract_text_from_chars(item['detail_title_chars'])
        notes = transliterate_number(notes)
        print(f"Notes: {notes}")
        
        for row in item['quran_ten_word_mp3']:
            id = row['reading_order']
            file_path = row['file']
            reading = extract_text_from_chars(row['detail_chars'])
            print(f"ID: {id}")
            #to print the audio file path print(f"File Path: {file_path}")
            reading = reading.replace('ابنsعامر', 'ابن عامر').replace('أبوsجعفر', 'أبو جعفر').replace('أبوsعمرو', 'أبو عمرو')
            
            print(f"Reading: {reading}")
        # print("\n" + "-"*50 + "\n")