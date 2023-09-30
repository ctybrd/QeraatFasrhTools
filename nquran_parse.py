import os
import sqlite3
from bs4 import BeautifulSoup

# Function to extract Sora and Aya numbers from the file name
def extract_sora_aya(filename):
    parts = os.path.splitext(filename)[0].split('_')
    sora = int(parts[0].replace('Sora', ''))
    aya = int(parts[1].replace('Aya', ''))
    return sora, aya

# Initialize SQLite database and table
conn = sqlite3.connect('quran_data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS quran_data (
        sora INTEGER,
        aya INTEGER,
        content TEXT
    )
''')

# Directory containing HTML files
html_dir = 'E:/Qeraat/QeraatFasrhTools_Data/nQuran'

# Iterate through HTML files
for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
        # Extract Sora and Aya numbers from the file name
        sora, aya = extract_sora_aya(filename)

        # Read the HTML file
        with open(os.path.join(html_dir, filename), 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'lxml')
        detail_div = soup.find('div', id='detail')
        if detail_div:
            # Extract content from sub-sections with class 'quran-page'
            quran_pages = detail_div.find_all(class_='quran-page')
            for i, quran_page in enumerate(quran_pages, start=1):
                content = quran_page.get_text()
                
                # Insert data into SQLite database
                cursor.execute('INSERT INTO quran_data (sora, aya, content) VALUES (?, ?, ?)',
                               (sora, aya, content))
                print(f'Inserted Sora {sora}, Aya {aya}, Page {i}')

# Commit and close the database connection
conn.commit()
conn.close()
