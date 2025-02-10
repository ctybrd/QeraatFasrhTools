import sqlite3
from docx import Document

# File paths
word_file = r"E:\Qeraat\QeraatFasrhTools\ShmrlyWord\Shamarly0.docx"
db_file = r"E:\Qeraat\QeraatFasrhTools\QeraatSearch\qeraat_data_simple.db"

# Connect to SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Clear existing table data
cursor.execute("DELETE FROM first_words")
conn.commit()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS first_words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pageno INTEGER,
    lineno INTEGER,
    first_word TEXT,
    second_word TEXT
)
""")

# Read the Word document
doc = Document(word_file)

page_no = 1
line_no = 1  # Start from line 1
page_lines = []

# Loop through paragraphs in the document
for para in doc.paragraphs:
    text = para.text.strip()

    # Detect manual page breaks
    if para._element.getparent().tag.endswith('sectPr'):  # Detects new sections/pages
        # Save previous page data
        if page_lines:
            cursor.executemany("INSERT INTO first_words (pageno, lineno, first_word, second_word) VALUES (?, ?, ?, ?)", page_lines)
            conn.commit()
            page_lines = []

        # Increment page number and reset line number
        page_no += 1
        line_no = 1
        continue

    # Skip completely empty paragraphs but maintain the line count
    if not text:
        page_lines.append((page_no, line_no, None, None))
        line_no += 1
        continue

    words = text.split()
    first_word = words[0] if len(words) > 0 else None
    second_word = words[1] if len(words) > 1 else None

    # Store the extracted words
    page_lines.append((page_no, line_no, first_word, second_word))
    line_no += 1

# Insert remaining lines for the last page
if page_lines:
    cursor.executemany("INSERT INTO first_words (pageno, lineno, first_word, second_word) VALUES (?, ?, ?, ?)", page_lines)
    conn.commit()

conn.close()
print("Data successfully inserted into the database.")
