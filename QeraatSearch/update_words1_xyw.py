import sqlite3
import pandas as pd

def update_words_with_margins(db_path, words_data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Margins and spacing
    left_margin = 0.05
    right_margin = 0.05
    inter_word_margin = 0.01

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
            if row['wordsno'] in [999, 1000]:
                # Fixed width for landmarks
                width = row['rawword_length']
            else:
                # Proportional width for regular words
                width = row['rawword_length'] / total_raw_width * (1 - total_margin_space) if total_raw_width else 0

            # Calculate x and update for the next word
            x = x_position - width
            x_position = x - inter_word_margin  # Update x_position for the next word

            # Update the wordsall table
            update_query = """
            UPDATE wordsall
            SET x = ?, y = ?, width = ?
            WHERE wordindex = ? AND wordsno = ?
            """
            cursor.execute(update_query, (
                round(x, 6),
                y_positions.get(int(lineno), 0),
                round(width, 6),
                int(row['wordindex']),
                int(row['wordsno'])
            ))

    try:
        conn.commit()
        print("Update complete.")
    except sqlite3.Error as e:
        print(f"Error updating data: {e}")
    finally:
        conn.close()

# Main execution

db_path = r'D:\\Qeraat\\QeraatFasrhTools\\QeraatSearch\\qeraat_data_simple.db'
query = "SELECT * FROM wordsall ORDER BY wordindex, wordsno"

words_data = pd.read_sql_query(query, sqlite3.connect(db_path))

# Calculate word lengths, assigning fixed lengths for landmarks and regular lengths for others
words_data['rawword_length'] = words_data.apply(
    lambda row: 0.05 if row['wordsno'] == 999 else (0.03 if row['wordsno'] == 1000 else len(row['rawword'])),
    axis=1
)

# Define y positions for lines
y_positions = {
    1: 0.0878, 2: 0.1537, 3: 0.2172, 4: 0.2802, 5: 0.3463,
    6: 0.4108, 7: 0.4782, 8: 0.537, 9: 0.6012, 10: 0.6658,
    11: 0.7293, 12: 0.7932, 13: 0.8525, 14: 0.9176, 15: 0.9831
}

# Run the update function
update_words_with_margins(db_path, words_data)