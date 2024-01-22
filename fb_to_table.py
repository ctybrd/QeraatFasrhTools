from functools import partial
import sqlite3
import json
import re
from datetime import datetime

fix_mojibake_escapes = partial(
     re.compile(rb'\\u00([\da-f]{2})').sub,
     lambda m: bytes.fromhex(m[1].decode()),
 )


# Load the JSON data from the file
with open('fb.json', 'rb') as binary_data:
     repaired = fix_mojibake_escapes(binary_data.read())
data = json.loads(repaired)

# Connect to SQLite database (create if not exists)
conn = sqlite3.connect('facebook_posts.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp INTEGER,
        real_datetime TEXT,
        post_text TEXT,
        hashtags TEXT
    )
''')

# Parse and insert data into the SQLite table
for entry in data:
    timestamp = entry.get('timestamp')
    real_datetime = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    posts_data = entry.get('data', [])
    
    for post_entry in posts_data:
        post_text = post_entry.get('post', '')
        # Extract hashtags from the post text
        hashtags = [word[1:] for word in post_text.split() if word.startswith('#')]
        hashtags_str = ' '.join(hashtags)
        
        # Insert data into the table
        cursor.execute('''
            INSERT INTO posts (timestamp, real_datetime, post_text, hashtags)
            VALUES (?, ?, ?, ?)
        ''', (timestamp, real_datetime, post_text, hashtags_str))

# Commit the changes and close the connection
conn.commit()
conn.close()
