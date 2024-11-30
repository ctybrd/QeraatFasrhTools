import sqlite3
import re

# File paths
db_path = r"e:\Qeraat\QeraatFasrhTools\qeraatSearch\qeraat_data_simple.db"
txt_file_path = r"e:\Qeraat\QeraatFasrhTools\quran_txt.txt"
output_file_path = r"e:\Qeraat\QeraatFasrhTools\quran_with_breaks.txt"

# Arabic-Indic numerals and special words to ignore in counting
excluded_words = {'۞', '۩'}
arabic_numerals_pattern = r'[١٢٣٤٥٦٧٨٩٠]+'  # Regular expression to match Arabic numerals (1 or more)
excluded_set = excluded_words

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fetch words data
cursor.execute("""
    SELECT wordindex, word, page_number2, lineno2
    FROM words1
    WHERE wordindex NOT IN (1, 2, 3, 4, 30, 31, 32, 33)
    ORDER BY wordindex
""")
words_data = cursor.fetchall()
conn.close()

# Read the input text file
with open(txt_file_path, 'r', encoding='utf-8') as file:
    input_text = file.read()

# Split the text into words
text_words = input_text.split()

# Initialize output variables
output_text = []
current_page = None
current_line = None
line_words = []  # Collect words for the current line
word_count = 0

# Function to check if the word is an excluded word or contains Arabic numerals
def is_excluded(word):
    # Check if the word is in the excluded words list or matches Arabic numerals
    if word in excluded_words:
        return True
    if re.match(arabic_numerals_pattern, word):
        return True
    return False

# Process words from the database
for word_data in words_data:
    wordindex, db_word, page_number2, lineno2 = word_data

    # Handle Surah headers
    while word_count < len(text_words):
        current_word = text_words[word_count]

        # Handle surah headers
        if current_word.startswith('سُورَةُ'):
            output_text.append('\n')  # Add an empty line before surah header
            surah_header = ' '.join(text_words[word_count:word_count + 2])  # Surah header
            output_text.append(surah_header + '\n')  # Add surah header
            bismillah = ' '.join(text_words[word_count + 2:word_count + 6])  # Bismillah
            output_text.append(bismillah + '\n')  # Add Bismillah
            word_count += 6  # Skip surah header and Bismillah
            line_words = []  # Reset line words
            current_line = None  # Reset line tracking for the surah
            current_page = None  # Reset page tracking for the surah
            break

        # Skip excluded words
        if is_excluded(current_word):
            line_words.append(current_word)
            word_count += 1
            continue

        break

    # Add words to the current line
    if word_count < len(text_words):
        line_words.append(text_words[word_count])
        word_count += 1

        # Check if the line changes
        if lineno2 != current_line:
            if line_words:
                # Write the previous line's words to output
                output_text.append(' '.join(line_words) + '\n')
                line_words = []  # Reset line words

            current_line = lineno2

        # Check if the page changes
        if page_number2 != current_page:
            if current_page is not None:  # Avoid adding a page break at the start
                output_text.append('\f')  # Add page break
            current_page = page_number2

# Add remaining words in the last line
if line_words:
    output_text.append(' '.join(line_words) + '\n')

# Write the output to a file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(''.join(output_text))  # Avoid adding extra spaces

print(f"Output written to: {output_file_path}")
