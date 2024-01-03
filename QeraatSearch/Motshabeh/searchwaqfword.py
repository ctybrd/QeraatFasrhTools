import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('E:/Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db')
cursor = conn.cursor()

# Add a new column 'hamza' to the table
cursor.execute('ALTER TABLE book_quran_w ADD COLUMN hamza INTEGER')

# Execute the query to retrieve rows
cursor.execute('SELECT * FROM book_quran_w')

# Fetch all rows
rows = cursor.fetchall()

# Filter rows based on the last word containing Hamza characters
filtered_rows = [row for row in rows if any(char in row[3].split()[-1] for char in 'أؤئء')]

# Update the 'hamza' column to 1 for the matching rows
for row in filtered_rows:
    cursor.execute('UPDATE book_quran_w SET hamza = 1 WHERE part_id = ?', (row[0],))

# Commit the changes
conn.commit()

# Close the database connection
conn.close()
