import sqlite3
from unidecode import unidecode
#pip install pyarabic
import pyarabic.araby as araby

# Connect to the SQLite database
conn = sqlite3.connect('D:/Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db')
cursor = conn.cursor()

# Define the function to remove diacritics
#transliterates the word i better user strip diacritics
def remove_diacritics(text):
    rawtext=''.join([t for t in text if t not in ['ِ', 'ُ', 'ٓ', 'ٰ', 'ْ', 'ٌ', 'ٍ', 'ً', 'ّ', 'َ']])
    return unidecode(rawtext)

# Update the "rawword" column for existing rows
cursor.execute("SELECT wordindex, word FROM words1")
rows = cursor.fetchall()
for row in rows:
    wordindex, word = row
    rawword = araby.strip_diacritics(word)
    cursor.execute("UPDATE words1 SET rawword = ? WHERE wordindex = ?", (rawword, wordindex))

# Commit the changes and close the connection
conn.commit()
conn.close()