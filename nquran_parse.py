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

# Initialize variables to track the current Sora and Aya
current_sora = None
current_aya = None
custom_serial = 1

# Iterate through HTML files while maintaining order
html_files = sorted(os.listdir(html_dir))
for i, filename in enumerate(html_files[:10], start=1):
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
            # Extract content from sub-sections with class 'quran-page'
            quran_pages = detail_div.find_all(class_='quran-page')
            
            # Extract subject and sub-subject information
            selectquran_tags = detail_div.find_all('div', class_='selectquran')
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
                
                # Check if there are enough selectquran divs
                if j <= len(selectquran_tags):
                    subject = extract_subject(selectquran_tags[j - 1])  # Use the corresponding selectquran div
                else:
                    subject = None
                
                # Extract sub-subjects
                sub_subjects = extract_sub_subject(selectquran_tags[j - 1]) if j <= len(selectquran_tags) else []
                
                # Extract the first item as qarees
                content = content.replace(', عن,', ' عن')
                qarees = None
                if content:
                    content_split = content.split('\r\n', 1)  # Split into lines
                    if len(content_split) > 1:
                        qarees = content_split[0]  # Get the first line

                # Extract the last item as reading
                reading = None
                if content:
                    content_split = content.split('\r\n')  # Split into lines
                    if len(content_split) > 1:
                        reading = content_split[-1]  # Get the last line
                    
                # Insert data into SQLite database with compound primary key
                for sub_subject in sub_subjects:                   
                    cursor.execute('INSERT OR IGNORE INTO quran_data (id, sora, aya, subject, sub_subject, content, qarees, reading) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                                   (custom_serial, sora, aya, subject, sub_subject, content, qarees, reading))
                    print(f'Inserted Sora {sora}, Aya {aya}, Subject: {subject}, Sub-Subject: {sub_subject}, Page {j}, Custom Serial: {custom_serial}')

                    custom_serial += 1  # Increment custom serial within the same Sora or Aya

# Commit and close the database connection
conn.commit()
conn.close()
