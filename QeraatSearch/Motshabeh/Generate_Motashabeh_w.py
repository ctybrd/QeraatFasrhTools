import sqlite3
import nltk
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download the Arabic stopwords if not already downloaded
nltk.download('stopwords')
nltk.download('punkt')

def calculate_word_overlap(text1, text2):
    # Tokenize and remove stopwords for Arabic text
    stop_words = set(stopwords.words('arabic'))
    tokens1 = [word for word in word_tokenize(text1) if word not in stop_words]
    tokens2 = [word for word in word_tokenize(text2) if word not in stop_words]

    # Calculate word overlap
    overlap = len(set(tokens1) & set(tokens2))

    # Normalize by the average length of the two texts
    normalized_overlap = overlap / ((len(tokens1) + len(tokens2)) / 2 + 1)

    return normalized_overlap

# Connect to the SQLite database
db_path = r'E:/Qeraat/QeraatFasrhTools/QeraatSearch/Motshabeh/motshabeh.db'
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Truncate the similarity table if it exists
cursor.execute("DROP TABLE IF EXISTS similarity_matrix")
connection.commit()

# Create the similarity matrix table
cursor.execute("CREATE TABLE similarity_matrix (index1 INTEGER, index2 INTEGER, similarity_score REAL, pid1 INTEGER, pid2 INTEGER)")

# Retrieve all verses from the database
cursor.execute("SELECT aya_index, part_id, part_text FROM book_quran_w")
verses = cursor.fetchall()

# Calculate and store similarities
total_verses = len(verses)

# Set a similarity tolerance
tolerance = 0.5

for i in range(total_verses - 1):  # Start from the first verse and go up to the second-to-last verse
    print(f"Processing verse {i + 1}/{total_verses}")

    current_index, current_part, current_verse = verses[i]

    for j in range(i + 1, total_verses):  # Start from the next verse to the end
        comp_index, comp_part, comp_verse = verses[j]

        similarity_score = calculate_word_overlap(current_verse, comp_verse)

        # Check if similarity is above the tolerance threshold
        if similarity_score > tolerance:
            # Insert the similarity score into the table
            cursor.execute("INSERT INTO similarity_matrix VALUES (?, ?, ?, ?, ?)",
                           (current_index, comp_index, similarity_score, current_part, comp_part))

            # Print information about the verses being compared
            print(f"Aya {current_index} ({current_verse}) is similar to Aya {comp_index} ({comp_verse}) with a similarity score of {similarity_score}")

# Commit the changes to the database
connection.commit()

# Close the database connection
connection.close()
