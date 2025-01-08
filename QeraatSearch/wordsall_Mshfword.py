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
doc_path = drive + "Qeraat/QeraatFasrhTools/Quran.docx"

# Step 1: Parse the Word document
def extract_tokens(doc_path):
    doc = Document(doc_path)
    tokens = []
    bismillah_count = 0  # Track occurrences of "بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ"
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if text.startswith("سُورَةُ"):
            continue  # Skip surah headers
        
        if text.startswith("بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ") or text.startswith("بِّسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ"):
            bismillah_count += 1
            if bismillah_count > 2:  # Skip after the second occurrence
                continue
        
        if text:
            tokens.extend(text.split())  # Split into tokens
    return tokens

# Step 2: Remove diacritics from Arabic text
def remove_diacritics(text):
    return araby.strip_diacritics(text)

# Step 3: Update the database with token matching
def update_database(db_path, tokens):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Fetch rows to update in order
        cursor.execute("SELECT wordindex, wordsno, rawword FROM wordsall where wordsno <> 1000 ORDER BY wordindex, wordsno")
        db_rows = cursor.fetchall()

        if len(tokens) < len(db_rows):
            print(f"Warning: Fewer tokens ({len(tokens)}) than database rows ({len(db_rows)}). Missing tokens will be handled.")
        
        token_index = 0  # Track the current token index
        previous_token = None  # Track the previous token for `wordsno = 1000`

        # Update the table row by row
        for wordindex, wordsno, rawword in db_rows:
            if wordsno == 1001:
                # Handle `wordsno = 1001`: Check for token or fill with ۞
                if token_index < len(tokens) and tokens[token_index] == '۞':
                    token = tokens[token_index]
                    cursor.execute("""
                        UPDATE wordsall 
                        SET mshfword = ?, mshfrawword = ?
                        WHERE wordindex = ? AND wordsno = ?
                    """, (token, token, wordindex, wordsno))
                    token_index += 1  # Consume token
                else:
                    cursor.execute("""
                        UPDATE wordsall 
                        SET mshfword = ?, mshfrawword = ?
                        WHERE wordindex = ? AND wordsno = ?
                    """, ('۞', '۞', wordindex, wordsno))
                continue  # Skip to the next row

            # elif wordsno == 1000 and previous_token:
            #     # Handle `wordsno = 1000`: Extract and assign ۩ from previous token
            #     if previous_token.endswith('۩'):
            #         mark = '۩'
            #         cursor.execute("""
            #             UPDATE wordsall 
            #             SET mshfword = ?, mshfrawword = ?
            #             WHERE wordindex = ? AND wordsno = ?
            #         """, (mark, mark, wordindex, wordsno))
            #     continue  # Skip to the next row

            elif token_index < len(tokens):
                # Regular token assignment
                token = tokens[token_index]
                normalized_token = remove_diacritics(token)
                normalized_rawword = remove_diacritics(rawword)

                cursor.execute("""
                    UPDATE wordsall 
                    SET mshfword = ?, mshfrawword = ?
                    WHERE wordindex = ? AND wordsno = ?
                """, (token, normalized_token, wordindex, wordsno))

                # Update tracking variables
                previous_token = token
                token_index += 1
            else:
                print(f"Out of tokens: No token available for wordindex={wordindex}, wordsno={wordsno}.")
                break
        
        conn.commit()
        print("Database update completed.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

# Execute the script
tokens = extract_tokens(doc_path)
update_database(db_path, tokens)
