import os
from functools import partial
import sqlite3
import json
import re
from datetime import datetime
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Fix Mojibake escapes
fix_mojibake_escapes = partial(
    re.compile(rb'\\u00([\da-f]{2})').sub,
    lambda m: bytes.fromhex(m[1].decode()),
)

filename = 'e:/facebook/your_facebook_activity/posts/your_posts__check_ins__photos_and_videos_1.json'

# Step 1: Read the file in binary mode and fix encoding issues
with open(filename, 'rb') as binary_data:
    repaired = fix_mojibake_escapes(binary_data.read())
    json_str = repaired.decode('utf-8', errors='replace')

# Step 2: Load the JSON data
try:
    data = json.loads(json_str)
except json.JSONDecodeError as e:
    print("Error parsing JSON:", e)
    exit()

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
        hashtags TEXT,
        title TEXT
    )
''')

# Clear existing records from the table
cursor.execute('DELETE FROM posts')

# Parse and insert data into the SQLite table
for entry in data:
    timestamp = entry.get('timestamp')
    real_datetime = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    posts_data = entry.get('data', [])
    title = entry.get('title', '')

    for post_entry in posts_data:
        post_text = post_entry.get('post', '')
        if post_text:
            hashtags = [word[1:] for word in post_text.split() if word.startswith('#')]
            hashtags_str = ', '.join(hashtags)
            cursor.execute('''
                INSERT INTO posts (timestamp, real_datetime, post_text, hashtags, title)
                VALUES (?, ?, ?, ?, ?)
            ''', (timestamp, real_datetime, post_text, hashtags_str, title))

# Commit the changes
conn.commit()

# Create output folder for Word documents
output_folder = 'output_documents'
os.makedirs(output_folder, exist_ok=True)

# Function to sanitize filenames
def sanitize_filename(filename):
    # Remove invalid characters for Windows
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

# Generate Word documents for each unique hashtag
cursor.execute("SELECT DISTINCT hashtags FROM posts")
all_hashtags = set()
for row in cursor.fetchall():
    hashtags = row[0].split(', ')
    all_hashtags.update(hashtags)

print("Generating Word documents...")

for hashtag in all_hashtags:
    sanitized_hashtag = sanitize_filename(hashtag)
    doc = Document()
    doc.add_heading(f'Posts for #{hashtag}', level=1)

    cursor.execute("SELECT real_datetime, post_text FROM posts WHERE hashtags LIKE ?", (f'%{hashtag}%',))
    posts = cursor.fetchall()

    if not posts:
        continue

    for real_datetime, post_text in posts:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(f"{real_datetime}\n{post_text}")
        run.font.size = Pt(12)
        doc.add_paragraph()  # Add a blank line between posts

    # Save the document for this hashtag
    filename = os.path.join(output_folder, f'hashtag_{sanitized_hashtag}.docx')
    doc.save(filename)
    print(f"Document created: {filename}")

# Close the database connection
conn.close()

print("All Word documents have been successfully generated in the 'output_documents' folder.")
