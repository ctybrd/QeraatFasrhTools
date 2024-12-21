import sqlite3
import pandas as pd

def update_words_with_margins(db_path, words_data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Margins and spacing
    # left_margin = 0.03
    # right_margin = 0.05
    inter_word_margin = 0.01

    # Process each line grouped by page_number and lineno
    for (page_number, lineno), line_data in words_data.groupby(['page_number2', 'lineno2']):
        print(f"Processing page {page_number}, line {lineno} with {len(line_data)} words.")  # Debug log
        if page_number % 2 == 0:  # Even pages
            left_margin = 0.03
            right_margin = 0.03
        else:    
            left_margin = 0.02
            right_margin = 0.04
        # Calculate total margin space
        num_words = len(line_data)
        total_margin_space = left_margin + right_margin + (num_words - 1) * inter_word_margin

        # Separate fixed and proportional words
        fixed_words = line_data[line_data['wordsno'].isin([999, 1000, 1001])]
        proportional_words = line_data[~line_data['wordsno'].isin([999, 1000, 1001])]

        # Step 1: Calculate widths
        fixed_total_width = fixed_words['rawword_length'].sum()
        remaining_width = 1 - total_margin_space - fixed_total_width  # Total width left for proportional words

        if remaining_width < 0:
            print("Warning: Not enough space for proportional words.")  # Debug
            remaining_width = 0  # Handle edge cases gracefully

        # Assign proportional widths
        proportional_total_raw_width = proportional_words['rawword_length'].sum()
        if proportional_total_raw_width > 0:
            proportional_words['width'] = (
                proportional_words['rawword_length'] / proportional_total_raw_width * remaining_width
            )
        else:
            proportional_words['width'] = 0

        # Combine fixed and proportional words
        line_data = pd.concat([fixed_words, proportional_words]).sort_index()

        # Step 2: Calculate x positions
        x_position = 1 - right_margin  # Start at the right-most margin
        for idx, row in line_data.iterrows():
            width = row['width'] if 'width' in row else row['rawword_length']
            x = x_position - width  # Current word's x position
            x_position = x - inter_word_margin  # Update for the next word

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
query = "SELECT * FROM wordsall where wordindex>11629 and page_number2<530 ORDER BY wordindex, wordsno"

words_data = pd.read_sql_query(query, sqlite3.connect(db_path))

# Calculate word lengths, assigning fixed lengths for landmarks and regular lengths for others
# Pre-fetch the relevant pages for wordsno=1001 to improve efficiency
#علامة الربع غير موجودة لأوائل السور
conn = sqlite3.connect(db_path)
query = """
select distinct page_number2 from wordsall where wordsno=1001 and aya_index
=(SELECT max(aya_index) from mosshf_shmrly where mosshf_shmrly.sora_number=wordsall.surah)
"""
eligible_pages = pd.read_sql_query(query, conn)['page_number2'].tolist()
conn.close()

# Assign rawword_length based on conditions
words_data['rawword_length'] = words_data.apply(
    lambda row: 0.05 if row['wordsno'] == 999 else
                (0.03 if row['wordsno'] == 1000 else
                (0.001 if row['wordsno'] == 1001 and row['page_number2'] in eligible_pages else
                 (0.02 if row['wordsno'] == 1001 else len(row['rawword'])))),
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
