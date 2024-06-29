import json

# Path to the JSON file
file_path = 'D:/Qeraat/QeraatFasrhTools_Data/Ten_Readings/json/Qeraat_303.json'

# Characters to be removed
chars_to_remove = "ﮎﮍﭜﮖﭝsﭨ﴿﴾ﭶﮅﮗﮘﯺﮔﯡﰃ"

# Create a translation table
translation_table = str.maketrans('', '', chars_to_remove)

# Function to extract text from chars and remove unwanted characters
def extract_text_from_chars(chars):
    text = ''.join([char['unicode'] for char in chars])
    return text #.translate(translation_table)

# Read and process the JSON file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

    for item in data:
        word_text = item['word_text'].translate(translation_table)
        print(f"الكلمة: {word_text}")
        
        detail_text = extract_text_from_chars(item['detail_title_chars'])
        print(f"ملاحظة: {detail_text}")
        
        for reading in item['quran_ten_word_mp3']:
            reading_order = reading['reading_order']
            file_path = reading['file']
            reading_detail_text = extract_text_from_chars(reading['detail_chars'])
            print(f"ترتيب: {reading_order}")
            #to print the audio file path print(f"File Path: {file_path}")
            reading_detail_text = reading_detail_text.replace('ابنعامر', 'ابن عامر').replace('أبوجعفر', 'أبو جعفر').replace('أبوعمرو', 'أبو عمرو')
            print(f"الفرش: {reading_detail_text}")
        print("\n" + "-"*50 + "\n")
