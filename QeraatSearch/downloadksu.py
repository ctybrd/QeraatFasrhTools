import sqlite3
import requests
import urllib3

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Database and table configuration
db_path = 'D:\\Qeraat\\QeraatFasrhTools\\QeraatSearch\\qeraat_data_simple.db'
site = 'en_sh'
table = 'ksu_tafsir'

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the new table if it doesn't exist
cursor.execute(f'''
CREATE TABLE IF NOT EXISTS book_{table} (
    aya_index INTEGER PRIMARY KEY,
    text TEXT
)
''')
conn.commit()

# Fetch the total number of verses in each surah
cursor.execute("SELECT sora, MAX(aya) AS total_ayas FROM book_quran GROUP BY sora")
surah_info = {row[0]: row[1] for row in cursor.fetchall()}  # {sora: total_ayas}

# Fetch all records from the book_quran table
cursor.execute("SELECT aya_index, sora, aya FROM book_quran ORDER BY aya_index")
records = cursor.fetchall()

# Function to download content
def download_content(sora, aya, next_aya, next_sora):
    """
    Fetch tafsir for the given sura and aya, ending at next_aya in next_sora.
    """
    url = f'https://quran.ksu.edu.sa/interface.php?ui=pc&do=tarjama&tafsir={site}&b_sura={sora}&b_aya={aya}&e_sura={next_sora}&e_aya={next_aya}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            json_data = response.json()
            tafsir_key = f"{sora}_{aya}"
            return json_data.get("tafsir", {}).get(tafsir_key, {}).get("text", None)
        else:
            print(f"Failed to fetch data for sora {sora} aya {aya}. HTTP Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return None

# Iterate through each record and fetch tafsir content
for record in records:
    aya_index, sora, aya = record
    total_ayas = surah_info[sora]

    # Calculate e_aya and e_sura
    if aya < total_ayas:  # Not the last aya in the surah
        next_aya = aya + 1
        next_sora = sora
    else:  # Last aya in the surah
        next_aya = 1
        next_sora = sora + 1 if sora < max(surah_info.keys()) else sora  # Stay at last surah

    # Fetch tafsir content
    content = download_content(sora, aya, next_aya, next_sora)
    if content:
        cursor.execute(f'INSERT OR IGNORE INTO book_{table} (aya_index, text) VALUES (?, ?)', (aya_index, content))
        conn.commit()
        print(f'Successfully inserted content for sora {sora} aya {aya}')
    else:
        print(f'No content found for sora {sora} aya {aya}')

# Update the table content to format specific text
conn.execute(f"UPDATE book_{table} SET text = REPLACE(REPLACE(text, '﴿', '<b>'), '﴾', '</b>')")
conn.commit()

# Close the database connection
conn.close()
