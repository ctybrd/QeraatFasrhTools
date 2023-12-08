import sqlite3
import re
# Connect to the SQLite database
conn = sqlite3.connect("E:/Qeraat/QeraatFasrhTools/QeraatSearch/Motshabeh/motshabeh.db")
cursor = conn.cursor()

# Create a new table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS book_quran_w (
        part_id INTEGER PRIMARY KEY AUTOINCREMENT,
        aya_index INTEGER,
        part_no INTEGER,
        part_text TEXT,
        part_text_full TEXT
    )
''')

# Fetch the rows from the original table
cursor.execute('SELECT aya_index, text_waqf FROM book_quran')
rows = cursor.fetchall()

# Specify the Unicode characters for splitting
#صلي و قلي وج وم
split_characters = ['\u06D6', '\u06D7', '\u06FF', '\u06D8','\u06DA']

# Function to remove diacritics from Arabic text
def remove_diacritics(text):
    diacritics = '[\u064b-\u0652]'
    return re.sub(diacritics, '', text)
cursor.execute(''' delete from book_quran_w''')
conn.commit()
# Insert data into the new table
part_id = 1
for row in rows:
    aya_index, text_waqf = row
    parts = re.split('|'.join(split_characters), text_waqf)
    for part_no, part_text_full in enumerate(parts, start=1):
        part_text = remove_diacritics(part_text_full)
        cursor.execute('''
            INSERT INTO book_quran_w (part_id,aya_index, part_no,part_text, part_text_full)
            VALUES (?, ?, ?, ?, ?)
        ''', (part_id,aya_index,part_no, part_text, part_text_full))
        part_id +=1

# Commit the changes and close the connection
conn.commit()
conn.close()
