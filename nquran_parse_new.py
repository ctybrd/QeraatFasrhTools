import os
import sqlite3
import re
from bs4 import BeautifulSoup

# Function to extract Sora and Aya numbers from the file name
def extract_sora_aya(filename):
    parts = os.path.splitext(filename)[0].split('_')
    sora = int(parts[0].replace('Sora', ''))
    aya = int(parts[1].replace('Aya', ''))
    return sora, aya

# Function to extract subject information
def extract_subject(selectquran_tag):
    subject_tag = selectquran_tag.find('strong')
    subject = subject_tag.get_text() if subject_tag else None
    return subject

# Function to extract sub-subject information
def extract_sub_subject(selectquran_tag):
    sub_subject_tags = selectquran_tag.find_all('div', class_='selectquran')
    sub_subjects = [tag.find('strong').get_text() if tag.find('strong') else None for tag in sub_subject_tags]
    return sub_subjects

# Initialize SQLite database and table
conn = sqlite3.connect('E:/Qeraat/QeraatFasrhTools_Data/nquran_data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS quran_data (
        id INTEGER,
        sora INTEGER,
        aya INTEGER,
        subject TEXT,
        sub_subject TEXT,
        content TEXT,
        qarees TEXT,
        reading TEXT,
        UNIQUE(sora, aya, id)
    )
''')

# Directory containing HTML files
html_dir = r'E:/Qeraat/QeraatFasrhTools_Data/nQuran'
all_rowa = [
    "نافع",
    "قالون_عن_نافع",
    "ورش_عن_نافع",
    "ابن كثير",
    "قنبل_عن_ابن كثير",
    "البزي_عن_ابن كثير",
    "أبو عمرو",
    "أبي عمرو",
    "السوسي_عن_أبي عمرو",
    "الدوري_عن_أبي عمرو",
    "ابن عامر",
    "هشام_عن_ابن عامر",
    "ابن ذكوان_عن_ابن عامر",
    "عاصم",
    "شعبة_عن_عاصم",
    "حفص_عن_عاصم",
    "حمزة",
    "خلف_عن_حمزة",
    "خلاد_عن_حمزة",
    "الكسائي",
    "أبو الحارث_عن_الكسائي",
    "الدوري_عن_الكسائي",
    "أبو جعفر",
    "أبي جعفر",
    "ابن وردان_عن_أبي جعفر",
    "ابن جماز_عن_أبي جعفر",
    "يعقوب",
    "رويس_عن_يعقوب",
    "روح_عن_يعقوب",
    "خلف العاشر",
    "كل الرواة",
    "باقي الرواة",   
]
# Create a dictionary to map main "rawy" to edited versions
rawy_mapping = {
    "نافع": "نافع",
    "قالون_عن_نافع": "نافع",
    "ورش_عن_نافع": "نافع",
    "ابن كثير": "ابن كثير",
    "قنبل_عن_ابن كثير": "ابن كثير",
    "البزي_عن_ابن كثير": "ابن كثير",
    "أبو عمرو": "أبو عمرو",
    "أبي عمرو": "أبو عمرو",
    "السوسي_عن_أبي عمرو": "أبو عمرو",
    "الدوري_عن_أبي عمرو": "أبو عمرو",
    "ابن عامر": "ابن عامر",
    "هشام_عن_ابن عامر": "ابن عامر",
    "ابن ذكوان_عن_ابن عامر": "ابن عامر",
    "عاصم": "عاصم",
    "شعبة_عن_عاصم": "عاصم",
    "حفص_عن_عاصم": "عاصم",
    "حمزة": "حمزة",
    "خلف_عن_حمزة": "حمزة",
    "خلاد_عن_حمزة": "حمزة",
    "الكسائي": "الكسائي",
    "أبو الحارث_عن_الكسائي": "الكسائي",
    "الدوري_عن_الكسائي": "الكسائي",
    "أبو جعفر": "أبو جعفر",
    "أبي جعفر": "أبو جعفر",
    "ابن وردان_عن_أبي جعفر": "أبو جعفر",
    "ابن جماز_عن_أبي جعفر": "أبو جعفر",
    "يعقوب": "يعقوب",
    "رويس_عن_يعقوب": "يعقوب",
    "روح_عن_يعقوب": "يعقوب",
    "خلف العاشر": "خلف العاشر",
    "كل الرواة": "كل الرواة",
    "باقي الرواة": "باقي الرواة",
}


# Initialize variables to track the current Sora and Aya
current_sora = None
current_aya = None
custom_serial = 1

# Iterate through HTML files while maintaining order
html_files = sorted(os.listdir(html_dir))
# for i, filename in enumerate(html_files[:10], start=1):
for i, filename in enumerate(html_files, start=1):
    if filename.endswith('.html'):
        # Extract Sora and Aya numbers from the file name
        sora, aya = extract_sora_aya(filename)
        comma_around_an = re.compile(r',\s*عن,\s*')
        # Check if the Sora or Aya has changed
        if sora != current_sora or aya != current_aya:
            current_sora = sora
            current_aya = aya
            custom_serial = 1  # Reset custom serial for a new Sora or Aya
        
        # Read the HTML file
        with open(os.path.join(html_dir, filename), 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'lxml')
        detail_div = soup.find('div', id='detail')
        if detail_div:
            # Extract subject and sub-subject information
            selectquran_tags = detail_div.find_all('div', class_='selectquran')
            
            for selectquran_tag in selectquran_tags:
                # Extract content from sub-sections with class 'quran-page'
                quran_pages = selectquran_tag.find_all(class_='quran-page')

                # Extract subject
                subject = extract_subject(selectquran_tag)

                # Extract sub-subjects
                sub_subjects = extract_sub_subject(selectquran_tag)

                for j, quran_page in enumerate(quran_pages, start=1):
                    content_lines = [line.strip() for line in quran_page.stripped_strings]  # Get stripped lines

                    # Combine lines with "," separator
                    content = ', '.join(content_lines)

                    # Replace the last comma with a CR LF (newline character)
                    content = content.rsplit(', ', 1)
                    if len(content) > 1:
                        content = f'{content[0]}\r\n{content[1]}'
                    else:
                        content = content[0]
                    content = content.replace(', عن,', '_عن_')
                    last_match_index = None
                    for i, content_line in enumerate(content_lines):
                        for k, rawy in enumerate(all_rowa):
                            if content_line.endswith(rawy):
                                last_match_index = i
                    
                    # Extract qarees and reading based on the last match
                    if last_match_index is not None:
                        qarees_lines = content_lines[:last_match_index + 1]
                        reading_lines = content_lines[last_match_index + 1:]
                        qarees = ', '.join(qarees_lines)
                        reading = ', '.join(reading_lines) if reading_lines else None
                    else:
                        qarees = None
                        reading = content  # If no match, consider the entire content as reading
                    if qarees:
                        qarees = qarees.replace(', عن,', '_عن_')
                    # Insert data into SQLite database with compound primary key
                    for sub_subject in sub_subjects:
                        cursor.execute('INSERT OR IGNORE INTO quran_data (id, sora, aya, subject, sub_subject, content, qarees, reading) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                                       (custom_serial, sora, aya, subject, sub_subject, content, qarees, reading))
                        print(f'Inserted Sora {sora}, Aya {aya}, Subject: {subject}, Sub-Subject: {sub_subject}, Page {j}, Custom Serial: {custom_serial}')

                        custom_serial += 1  # Increment custom serial within the same Sora or Aya

# Commit and close the database connection
conn.commit()
conn.close()
# remove extra رقم الآية text
# UPDATE quran_data
# SET subject = SUBSTR(subject, 1, INSTR(subject, '- رقم الآية:') - 1)
# WHERE INSTR(subject, '- رقم الآية:') > 0;
#remove curly braces
# UPDATE quran_data
# SET subject = REPLACE(REPLACE(subject, '{', ''), '}', ''),
#    sub_subject = REPLACE(REPLACE(sub_subject, '{', ''), '}', '');

# update quran_data set page_number1=(SELECT mosshf_madina.page_number  from mosshf_madina where aya_number= quran_data.aya and sora_number=quran_data.sora)
# update quran_data set page_number2=(SELECT mosshf_shmrly.page_number  
# from mosshf_shmrly where aya_number= quran_data.aya and sora_number=quran_data.sora)