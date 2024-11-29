import sqlite3

# File paths
db_path = r"d:/Qeraat/QeraatFasrhTools/qeraatSearch/qeraat_data_simple.db"
txt_file_path = r"d:/Qeraat/QeraatFasrhTools/quran_txt.txt"
output_file_path = r"d:/Qeraat/QeraatFasrhTools/quran_with_breaks.txt"

# Arabic-Indic numerals and special words to ignore in counting
excluded_words = {'۞', '۩'}
arabic_numerals = {'١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩'}
excluded_set = excluded_words | arabic_numerals

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fetch words data
cursor.execute("""
    SELECT wordindex, word, page_number2, lineno2
    FROM words1
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
word_count = 0

# Process words from database
for word_data in words_data:
    wordindex, db_word, page_number2, lineno2 = word_data

    # Skip excluded words in the text file, but include them in the output
    while word_count < len(text_words) and text_words[word_count] in excluded_set:
        output_text.append(text_words[word_count])
        word_count += 1

    # Add the current word to the output
    if word_count < len(text_words):
        output_text.append(text_words[word_count])
        word_count += 1

        # Add line breaks if the line changes
        if lineno2 != current_line:
            output_text.append('\n')
            current_line = lineno2

        # Add page breaks if the page changes
        if page_number2 != current_page:
            output_text.append('\f')
            current_page = page_number2

# Add any remaining words from the text file (should not happen, but for completeness)
while word_count < len(text_words):
    output_text.append(text_words[word_count])
    word_count += 1

# Write the output to a new file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(' '.join(output_text))

print(f"Output written to: {output_file_path}")
