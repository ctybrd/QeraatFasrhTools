import sqlite3 
 
# connect to the database or create it 
conn = sqlite3.connect('quran.db') 
 
# create cursor 
cursor = conn.cursor() 
 
# create words table 
cursor.execute('CREATE TABLE IF NOT EXISTS words (word TEXT, surah INTEGER, ayah INTEGER)') 
 
# open the Quran text file 
with open('quran.txt', 'r', encoding='utf-8') as f: 
    for line in f: 
        # split line into words 
        words1 =line.split('|') 
        words = words1[2].split() 
        # get surah and ayah from line 
        surah = words1[0]
        ayah = words1[0]
        # insert each word into words table 
        for word in words: 
            cursor.execute('INSERT INTO words (word, surah, ayah) VALUES (?, ?, ?)', (word, surah, ayah)) 
 
# save changes to the database 
conn.commit() 
 
# close database connection 
conn.close()