import json

# Path to the JSON file
file_path = 'e:/Qeraat/QeraatFasrhTools_Data/Ten_Readings/json/Qeraat_118.json'
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
        word_text = item['word_text']
        print(f"الكلمة: {word_text}")
        
        detail_text = extract_text_from_chars(item['detail_title_chars'])
        print(f"ملاحظة: {detail_text}")
        
        for reading in item['quran_ten_word_mp3']:
            reading_order = reading['reading_order']
            file_path = reading['file']
            reading_detail_text = extract_text_from_chars(reading['detail_chars'])
            print(f"ترتيب: {reading_order}")
            #to print the audio file path print(f"File Path: {file_path}")
            reading_detail_text = reading_detail_text.replace('ابنsعامر', 'ابن عامر').replace('أبوsجعفر', 'أبو جعفر').replace('أبوsعمرو', 'أبو عمرو')
            print(f"الفرش: {reading_detail_text}")
        print("\n" + "-"*50 + "\n")