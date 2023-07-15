import sqlite3
from docx import Document
import re

def replace_characters(text):
    text = text.replace("ﭼ", ")")
    text = text.replace("ﭽ", "(")
    return text

def parse_text_and_insert_to_database(text, page_number, cursor):
    matches = re.findall(r"(\d+)(.*?)((?=\d)|$)", text)
    
    for match in matches:
        number = match[0]
        current_text = match[1].strip()
        cursor.execute("INSERT INTO Hamza_Waqf (aya_number, text, page_number) VALUES (?, ?, ?)", (number, current_text, page_number))

def extract_text_next_to_keyword(doc_path, keyword):
    conn = sqlite3.connect("Hamza_Waqf_db.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Hamza_Waqf (aya_number INTEGER, text TEXT, page_number INTEGER)")
    cursor.execute("DELETE FROM Hamza_Waqf")

    document = Document(doc_path)
    page_number = 3
   
    for table in document.tables:
        incr =False
        for row in table.rows:
            for i in range(len(row.cells)):
                cell = row.cells[i]
                cell_text = cell.text.strip()
                if cell_text == 'السكت' or cell_text == 'الوقف' or cell_text == 'الإمالة':
                    incr =True
                if keyword == cell_text:
                    if i + 1 < len(row.cells):
                        next_cell = row.cells[i + 1]
                        next_cell_text = next_cell.text.strip()
                        replaced_text = replace_characters(next_cell_text)
                        print(page_number,replaced_text)
                        parse_text_and_insert_to_database(replaced_text, page_number, cursor)

        if incr:          
            page_number += 1
            

    conn.commit()
    conn.close()

# Provide the path to your Word document and the keyword
doc_path = "E:/Qeraat/AliSalehHamza.docx"
keyword = "الوقف"

extract_text_next_to_keyword(doc_path, keyword)
