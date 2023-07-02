import sqlite3

# Connect to the database
conn = sqlite3.connect('E:/Qeraat/QeraatFasrhTools/QuranWordMap/quran.db')
cursor = conn.cursor()

# Read the text file and insert words into the "words" table
with open('quran.txt', 'r', encoding='utf-8') as file:
    for line in file:
        surah, ayah, ayatext = line.strip().split('|')

        # Split the ayatext into words
        words = ayatext.split()

        # Insert each word into the "words" table
        for word in words:
            cursor.execute("INSERT INTO words (word, surah, ayah) VALUES (?, ?, ?)", (word, surah, ayah))

# Retrieve the pageno for each word from the "mosshf_shmrly" table
cursor.execute("SELECT sora_number, aya_number, page_number FROM mosshf_shmrly")
ayah_pages = cursor.fetchall()

# Update the words table with the corresponding pageno
for surah, ayah, page in ayah_pages:
    cursor.execute("UPDATE words SET pageno = ? WHERE surah = ? AND ayah = ?", (page, surah, ayah))

# Commit the changes and close the connection
conn.commit()
conn.close()
