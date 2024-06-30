import json
import os
import sqlite3

# Function to extract text from character list
def extract_text_from_chars(chars):
    return ''.join([char['unicode'] for char in chars]) if chars else ''

# Function to transliterate Arabic numbers to English numbers
def transliterate_number(number):
    mapping = {'٠':'0','١':'1','٢':'2','٣':'3','٤':'4','٥':'5','٦':'6','٧':'7', '٨':'8', '٩':'9',}
    return ''.join(mapping.get(char, char) for char in str(number))

# Folder containing JSON files
script_path = os.path.abspath(__file__)
drive, _ = os.path.splitdrive(script_path)
drive = drive +'/'
folder_path = os.path.join(drive, 'Qeraat/QeraatFasrhTools_Data/Ten_Readings/json')

# Connect to the SQLite database
db_path = os.path.join(drive, 'Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Clear the table before inserting new data
cursor.execute('DELETE FROM kw_data')
conn.commit()

# Loop over all JSON files in the folder
for file_name in os.listdir(folder_path):
    if file_name.startswith('Qeraat_') and file_name.endswith('.json'):
        page_number1 = int(file_name.split('_')[1].split('.')[0])
        file_path = os.path.join(folder_path, file_name)
        print(f"Processing file: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                sub_subject = item['word_text']
                notes = transliterate_number(extract_text_from_chars(item.get('detail_title_chars', [])))

                for row in item['quran_ten_word_mp3']:
                    id = row['reading_order']
                    reading = extract_text_from_chars(row.get('detail_chars', []))
                    reading = reading.replace('ابنsعامر', 'ابن عامر').replace('أبوsجعفر', 'أبو جعفر').replace('أبوsعمرو', 'أبو عمرو')
                    
                    # Split reading into readingresult and qareesrest
                    reading_parts = reading.split(':')
                    readingresult = reading_parts[0].strip() if len(reading_parts) > 0 else ''
                    qareesrest = reading_parts[1].strip() if len(reading_parts) > 1 else ''

                    # Insert data into the database
                    cursor.execute("""
                        INSERT INTO kw_data (id, sub_subject, reading, qareesrest, page_number1, page_number2, readingresult)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (id, sub_subject, reading, qareesrest, page_number1, None, readingresult))

            conn.commit()

# Close the database connection
conn.close()
