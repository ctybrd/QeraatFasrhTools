import sqlite3
import pandas as pd

# Connect to the SQLite database
db_path = r'D:\\Qeraat\\QeraatFasrhTools\\QeraatSearch\\qeraat_data_simple.db'
conn = sqlite3.connect(db_path)

# Delete previously auto-inserted lines
delete_query = "DELETE FROM shmrly_words WHERE circle='auto';"
cursor = conn.cursor()
cursor.execute(delete_query)

# Load words1 table into a pandas DataFrame
query = "SELECT * FROM words1 order by wordindex"
words_data = pd.read_sql_query(query, conn)

# Add a column for the rawword lengths
words_data['rawword_length'] = words_data['rawword'].apply(len)

# Define y positions for lines
y_positions = {
    1: 0.0878, 2: 0.1537, 3: 0.2172, 4: 0.2802, 5: 0.3463,
    6: 0.4108, 7: 0.4782, 8: 0.537, 9: 0.6012, 10: 0.6658,
    11: 0.7293, 12: 0.7932, 13: 0.8525, 14: 0.9176, 15: 0.9831
}

# Prepare the output list for insertions
output_rows = []

# Process each line grouped by page_number and lineno
for (page_number, lineno), line_data in words_data.groupby(['page_number2', 'lineno2']):
    total_width = line_data['rawword_length'].sum()
    x_position = 1 - 0.05  # Start from the right margin with 0.05 margin

    for index, row in line_data.iterrows():
        # Check if the word already exists in shmrly_words
        check_query = """
        SELECT 1 FROM shmrly_words WHERE wordindex = ?
        """
        cursor.execute(check_query, (row['wordindex'],))
        if cursor.fetchone():
            continue  # Skip if wordindex already exists

        # Calculate width as a ratio
        width = row['rawword_length'] / total_width if total_width else 0
        # Calculate x and update for next word
        x = x_position - width
        x_position = x - 0.02  # Add spacing of 0.02

        # Append the processed row
        output_rows.append({
            'qaree': 9,
            'page_number': page_number,
            'color': '#ff0000',
            'x': x,
            'y': y_positions.get(lineno, 0),
            'width': width,
            'style': 'S',
            'wordindex': row['wordindex'],
            'rawword': row['rawword'],
            'lineno': lineno,
            'surahno': row['surah'],
            'ayahno': row['ayah'],
            'ordr': row['wordsno'],
            'reallineno': lineno,
            'circle': 'auto'
        })

# Insert into shmrly_words table
insert_query = """
INSERT INTO shmrly_words 
(qaree, page_number, color, x, y, width, style, wordindex, rawword, lineno, surahno, ayahno, ordr, reallineno, circle)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# Execute the insertions
for row in output_rows:
    cursor.execute(insert_query, tuple(row.values()))

# Commit changes and close the connection
conn.commit()
conn.close()
