import sqlite3
import pandas as pd

def insert_words_with_margins(db_path, words_data):
    """Inserts words into the shmrly_words table with margin adjustments.

    Args:
        db_path: Path to the SQLite database.
        words_data: Pandas DataFrame containing word data.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Delete previously auto-inserted lines
    delete_query = "DELETE FROM shmrly_words WHERE circle='auto';"
    cursor.execute(delete_query)

    # Margins and spacing
    left_margin = 0.05
    right_margin = 0.05
    inter_word_margin = 0.02

    # Prepare the output list for insertions
    output_rows = []

    # Process each line grouped by page_number and lineno
    for (page_number, lineno), line_data in words_data.groupby(['page_number2', 'lineno2']):
        print(f"Processing page {page_number}, line {lineno} with {len(line_data)} words.")  # Debug log

        # Calculate total usable width
        total_raw_width = line_data['rawword_length'].sum()
        num_words = len(line_data)
        total_margin_space = left_margin + right_margin + (num_words - 1) * inter_word_margin
        total_width = total_raw_width + total_margin_space

        if total_width == 0:
            print("Skipped due to zero total width.")  # Debug
            continue

        # Initialize x position to start from the right-most position
        x_position = 1 - right_margin

        for _, row in line_data.iterrows():
            # Check if the word already exists in shmrly_words
            check_query = "SELECT 1 FROM shmrly_words WHERE wordindex = ?"
            cursor.execute(check_query, (row['wordindex'],))
            if cursor.fetchone():
                print(f"Word {row['rawword']} (index {row['wordindex']}) exists. Skipping.")  # Debug
                continue

            # Calculate width as a proportion of the total raw width
            width = row['rawword_length'] / total_raw_width * (1 - total_margin_space) if total_raw_width else 0

            # Calculate x and update for next word
            x = x_position - width
            x_position = x - inter_word_margin  # Update x_position for the next word

            # Append the processed row, ensuring correct column order
            output_rows.append((
                9,  # qaree
                int(page_number),  # page_number
                '#ff0000',  # color
                round(x, 6),  # x
                y_positions.get(int(lineno), 0),  # y
                round(width, 6),  # width
                'S',  # style
                int(row['wordindex']),  # wordindex
                row['rawword'],  # rawword
                int(lineno),  # lineno
                int(row['surah']),  # surahno
                int(row['ayah']),  # ayahno
                int(row['wordsno']),  # ordr
                int(lineno),  # reallineno
                'auto'  # circle
            ))

    # Insert into shmrly_words table
    insert_query = """
    INSERT INTO shmrly_words 
    (qaree, page_number, color, x, y, width, style, wordindex, rawword, lineno, surahno, ayahno, ordr, reallineno, circle)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    try:
        # Uncomment for bulk insert
        # cursor.executemany(insert_query, output_rows)

        # Use single inserts for debugging
        for row in output_rows:
            print("Inserting row:", row)  # Debug: Inspect each row
            cursor.execute(insert_query, row)

        conn.commit()
        print("Insertion complete.")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
    finally:
        conn.close()

# Main execution
db_path = r'D:\\Qeraat\\QeraatFasrhTools\\QeraatSearch\\qeraat_data_simple.db'
query = "SELECT * FROM words1 ORDER BY wordindex"
words_data = pd.read_sql_query(query, sqlite3.connect(db_path))

# Calculate word lengths
words_data['rawword_length'] = words_data['rawword'].apply(len)

# Define y positions for lines
y_positions = {
    1: 0.0878, 2: 0.1537, 3: 0.2172, 4: 0.2802, 5: 0.3463,
    6: 0.4108, 7: 0.4782, 8: 0.537, 9: 0.6012, 10: 0.6658,
    11: 0.7293, 12: 0.7932, 13: 0.8525, 14: 0.9176, 15: 0.9831
}

# Run the insertion function
insert_words_with_margins(db_path, words_data)
