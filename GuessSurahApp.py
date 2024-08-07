import sqlite3

# Path to the SQLite database file
db_path = 'D:/Qeraat/QeraatFasrhTools/QuranWordMap/quran.db'

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Define the SQL query to fetch the data
query = """
SELECT surahNo, group_concat(distinct ayahNo) as AyahNos
FROM WordCoordinate
WHERE ayahNo > 0
GROUP BY surahNo
ORDER BY count(distinct ayahNo)
"""

# Execute the query
cursor.execute(query)

# Fetch all results from the query
query_results = cursor.fetchall()

# Initialize the counter and set of used numbers
next_number = 1
used_numbers = set()
mapping = {}

# Process the query results
for surahNo, ayahNos in query_results:
    # Split the AyahNos string into individual numbers
    numbers = map(int, ayahNos.split(','))
    for num in numbers:
        if num not in used_numbers:
            # Assign the next available number and mark it as used
            mapping[num] = next_number
            used_numbers.add(num)
            next_number += 1

# Output the mapping
print(mapping)

# Create the new table 'ayamap' in the database
cursor.execute("DROP TABLE IF EXISTS ayamap")
cursor.execute("""
CREATE TABLE ayamap (
    ayahNo INTEGER PRIMARY KEY,
    mappedNumber INTEGER
)
""")

# Insert the mapping into the 'ayamap' table
for ayahNo, mappedNumber in mapping.items():
    cursor.execute("INSERT INTO ayamap (ayahNo, mappedNumber) VALUES (?, ?)", (ayahNo, mappedNumber))

# Commit the changes and close the connection
conn.commit()
conn.close()
