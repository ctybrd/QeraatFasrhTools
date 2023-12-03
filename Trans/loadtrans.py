import os
import re
import sqlite3
import pandas as pd

# Define the path to the folder containing the text files
folder_path = 'E:/Qeraat/QeraatFasrhTools/Trans/UserLanguages/Azerbaijani/Surrah/'

# SQLite database file
db_file = 'ayas_database.db'

# Initialize an empty list to store the data
data = []

# Initialize a global counter for aya_index
aya_index_counter = 1

# Loop through each text file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        # Extract language and number from the filename
        lang, number = re.match(r'([a-zA-Z]+)(\d+)', filename[:-4]).groups()

        # Read the content of the text file
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
            content = file.read()

            # Use regular expressions to extract aya information
            aya_matches = re.findall(r'(\d+)\.\s*(.*?)\s*(?=\d+\.)|(\d+)\.\s*(.*)$', content, re.DOTALL)

            # Append data to the list
            for aya_match in aya_matches:
                aya_number, aya_text = [group for group in aya_match if group]
                
                data.append({
                    'aya_index': aya_index_counter,
                    'sora': int(number),
                    'aya': int(aya_number),
                    'lang': lang,
                    'text': aya_text.strip()
                })

                # Increment the global aya_index counter
                aya_index_counter += 1

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Create an SQLite connection and cursor
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ayas (
        aya_index INTEGER,
        sora INTEGER,
        aya INTEGER,
        lang TEXT,
        text TEXT,
        PRIMARY KEY (aya_index)
    )
''')

# Insert data into the table
df.to_sql('ayas', conn, if_exists='replace', index=False)

# Commit changes and close the connection
conn.commit()
conn.close()
