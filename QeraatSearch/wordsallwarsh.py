import sqlite3
from docx import Document
import re
import os
import pyarabic.araby as araby

# Paths to the database and Word document
script_path = os.path.abspath(__file__)
drive, _ = os.path.splitdrive(script_path)
drive = drive + '/'
db_path = drive + "Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db"
doc_path = drive + "Qeraat/QeraatFasrhTools/UthmanicWarsh V21.docx"

# Arabic numeral conversion dictionary
arabic_numerals = {
    "٠": "0", "١": "1", "٢": "2", "٣": "3", "٤": "4", "٥": "5", "٦": "6", "٧": "7", "٨": "8", "٩": "9"
}

def convert_arabic_numerals(text):
    return int("".join(arabic_numerals.get(c, c) for c in text))

# Create the wordsall_warsh table if it doesn't exist and clear it at the start
def create_table():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wordsall_warsh (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wordindex INTEGER,
            wordsno INTEGER,
            rawword TEXT,
            mshfword TEXT,
            mshfrawword TEXT,
            surah INTEGER,
            ayah INTEGER
        )
    ''')
    cursor.execute("DELETE FROM wordsall_warsh")  # Clear the table
    conn.commit()
    conn.close()

# Parse the Word document
def extract_tokens(doc_path):
    doc = Document(doc_path)
    tokens = []
    surah_number = 0
    bismillah_count = 0  # Track occurrences of Basmala
    
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if text.startswith("سُورَةُ"):
            surah_number += 1
            tokens.append(("سُورَةُ", surah_number))
            continue  # Mark surah headers
        
        if text.startswith("بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ") or text.startswith("بِّسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ"):
            bismillah_count += 1
            if bismillah_count > 2:
                continue  # Skip after the second occurrence
        
        if text:
            tokens.extend([(word, surah_number) for word in text.split()])  # Split into words with surah number
    return tokens

# Remove diacritics from Arabic text
def remove_diacritics(text):
    return araby.strip_diacritics(text)

# Insert parsed words into the database
def insert_words_into_db(tokens):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    wordindex = 1
    wordsno = 1
    current_surah = 0
    current_ayah = 1
    last_wordsno_1_index = 1  # Tracks last wordindex with wordsno = 1
    ayah_updates = []  # Store ayah updates to apply later
    
    for i, (token, surah) in enumerate(tokens):
        if token == "سُورَةُ":
            current_surah = surah
            continue
        
        rawword = token
        mshfword = token
        mshfrawword = remove_diacritics(token)
        
        if re.match(r'^[٠-٩]+$', token):  # Arabic numerals only
            wordsno = 999
            current_ayah = convert_arabic_numerals(token)  # Convert Arabic to Western numerals
            ayah_updates.append((current_ayah, last_wordsno_1_index))  # Store ayah change
        elif token.endswith("۩"):  # If sajdah mark is attached to the word
            token = token[:-1]  # Remove sajdah mark from the word
            rawword = token
            mshfword = token
            mshfrawword = remove_diacritics(token)
            wordsno = wordsno + 1 if wordsno < 999 else 1
            if wordsno == 1:
                last_wordsno_1_index = wordindex
            
            cursor.execute('''
                INSERT INTO wordsall_warsh (wordindex, wordsno, rawword, mshfword, mshfrawword, surah, ayah)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (wordindex, wordsno, rawword, mshfword, mshfrawword, current_surah, current_ayah))
            
            cursor.execute('''
                INSERT INTO wordsall_warsh (wordindex, wordsno, rawword, mshfword, mshfrawword, surah, ayah)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (wordindex, 1000, "۩", "۩", "۩", current_surah, current_ayah))
        elif token == '۞':  # Ruku mark
            wordsno = 1001
        else:
            wordsno = wordsno + 1 if wordsno < 999 else 1  # Reset wordsno for new words
            if wordsno == 1:
                last_wordsno_1_index = wordindex  # Track latest wordsno = 1 occurrence
        
        cursor.execute('''
            INSERT INTO wordsall_warsh (wordindex, wordsno, rawword, mshfword, mshfrawword, surah, ayah)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (wordindex, wordsno, rawword, mshfword, mshfrawword, current_surah, current_ayah))
        
        if wordsno < 999:
            wordindex += 1  # Increment wordindex for normal words
    
    # Assign ayah numbers retroactively
    for ayah_number, start_index in ayah_updates:
        cursor.execute("UPDATE wordsall_warsh SET ayah = ? WHERE wordindex >= ? AND wordsno < 999", (ayah_number, start_index))
    conn.commit()
    # Correct wordindex for special marks
    cursor.execute("UPDATE wordsall_warsh SET wordindex = wordindex - 1 WHERE wordsno IN (999, 1000, 1001)")
    
    conn.commit()
    conn.close()

# Execute script
create_table()
tokens = extract_tokens(doc_path)
insert_words_into_db(tokens)
print("Database has been updated successfully.")
