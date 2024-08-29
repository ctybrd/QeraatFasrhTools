import sqlite3
import pandas as pd

# Connect to the SQLite database
db_path = 'D:/Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db'
conn = sqlite3.connect(db_path)
query = "SELECT rawword FROM words1"
df = pd.read_sql(query, conn)

# Function to find if two words differ by one letter in the same position
def one_letter_diff(word1, word2):
    if len(word1) != len(word2):
        return False
    diffs = sum(1 for a, b in zip(word1, word2) if a != b)
    return diffs == 1

# Prepare the new table
conn.execute('''
    CREATE TABLE IF NOT EXISTS words_groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pattern TEXT,
        word1 TEXT,
        word2 TEXT
    )
''')

# Group words and insert into the new table
for i, word1 in enumerate(df['rawword']):
    for j, word2 in enumerate(df['rawword']):
        if i >= j:
            continue
        if one_letter_diff(word1, word2):
            pattern = ''.join('_' if a != b else a for a, b in zip(word1, word2))
            conn.execute(
                "INSERT INTO words_groups (pattern, word1, word2) VALUES (?, ?, ?)",
                (pattern, word1, word2)
            )

# Commit the changes and close the connection
conn.commit()
conn.close()
