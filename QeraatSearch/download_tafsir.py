import sqlite3
import requests
from bs4 import BeautifulSoup

# Connect to the SQLite database
db_path = 'E:\\Qeraat\\QeraatFasrhTools\\QeraatSearch\\qeraat_data_simple.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the new table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS book_juzay (
    aya_index INTEGER,
    text TEXT
)
''')
conn.commit()

# Fetch all records from the book_quran table
cursor.execute('SELECT aya_index, sora, aya FROM book_quran where aya_index')
records = cursor.fetchall()

# Function to download the content of a webpage
def download_content(sora, aya):
    url = f'https://tafsir.app/altasheel/{sora}/{aya}'
    response = requests.get(url)
    if response.status_code == 200:
        # Use BeautifulSoup to parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the div with id="preloaded-text"
        preloaded_text_div = soup.find('div', id='preloaded-text')
        if preloaded_text_div:
            # Extract the text content
            content = preloaded_text_div.get_text(strip=True)
            return content
    return None

# Iterate through each record and download the webpage content
for record in records:
    aya_index, sora, aya = record
    content = download_content(sora, aya)
    if content:
        cursor.execute('INSERT INTO book_juzay (aya_index, text) VALUES (?, ?)', (aya_index, content))
        conn.commit()
        print(f'Successfully inserted content for sora {sora} aya {aya}')
    else:
        print(f'No content found for sora {sora} aya {aya}')

# Close the database connection
conn.close()
