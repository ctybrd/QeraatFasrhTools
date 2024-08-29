import json
import sqlite3
import os

def insert_data(cursor, data, pagenumber):
    """Inserts the JSON data into the SQLite database with hierarchical rows.

    Args:
        cursor: A SQLite cursor object.
        data: The JSON data to insert.
        pagenumber: The page number associated with the data.
    """

    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Hawamesh (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modified TEXT,
            order1 INTEGER,
            pagenumber INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Hawamesh_chars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            x0 REAL,
            x1 REAL,
            y0 REAL,
            y1 REAL,
            line INTEGER,
            size REAL,
            color TEXT,
            add_tab BOOLEAN,
            text_y0 REAL,
            text_y1 REAL,
            unicode TEXT,
            upright BOOLEAN,
            fontname TEXT,
            is_new_line BOOLEAN,
            add_single_space BOOLEAN,
            Hawamesh_id INTEGER,
            FOREIGN KEY(Hawamesh_id) REFERENCES Hawamesh(id)
        )
    ''')

    # Insert data into the main table (Hawamesh)
    for item in data:
        cursor.execute('''
            INSERT INTO Hawamesh (modified, order1, pagenumber)
            VALUES (?, ?, ?)
        ''', (item['modified'], item['order'], pagenumber))

        # Get the inserted row ID to use as a foreign key
        Hawamesh_id = cursor.lastrowid

        # Insert data into the child table (hawamesh_chars)
        for char_data in item.get('hawamesh_chars', []):
            color_data = json.dumps(char_data.get('color'))  # Convert color dict to JSON string
            cursor.execute('''
                INSERT INTO hawamesh_chars (
                    x0, x1, y0, y1, line, size, color, add_tab,
                    text_y0, text_y1, unicode, upright, fontname,
                    is_new_line, add_single_space, Hawamesh_id
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                char_data.get('x0'), char_data.get('x1'), char_data.get('y0'), char_data.get('y1'),
                char_data.get('line'), char_data.get('size'), color_data, char_data.get('add_tab'),
                char_data.get('text_y0'), char_data.get('text_y1'), char_data.get('unicode'),
                char_data.get('upright'), char_data.get('fontname'), char_data.get('is_new_line'),
                char_data.get('add_single_space'), Hawamesh_id
            ))

def main():
    """Reads JSON data from multiple files in a folder, inserts it into the database, and commits the changes."""

    folder_path = "d:/Qeraat/QeraatFasrhTools_Data/Ten_Readings/json"
    db_path = 'd:/Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db'
    
    # Establish a connection to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        for filename in os.listdir(folder_path):
            if filename.startswith("Hawamesh_") and filename.endswith(".json"):
                pagenumber = int(filename.split("_")[1].split(".")[0])  # Extract pagenumber from filename
                with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    insert_data(cursor, data, pagenumber)

        # Commit all changes to the database
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()  # Rollback changes if an error occurs
    finally:
        cursor.close()  # Close the cursor
        conn.close()  # Close the database connection

if __name__ == '__main__':
    main()
