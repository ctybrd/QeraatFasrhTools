
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

nltk.download('stopwords')

def calculate_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return similarity_matrix[0, 1]

def create_similarity_table(cursor, table_name):
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    cursor.execute(f"CREATE TABLE {table_name} (index1 INTEGER, index2 INTEGER, similarity_score REAL, word_length INTEGER)")

# Connect to the SQLite database
db_path = r'E:/Qeraat/QeraatFasrhTools/QeraatSearch/Motshabeh/motshabeh.db'
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Create the similarity matrix tables for different word lengths
word_lengths = [6,5,4,3,2]  # Add more lengths as needed
for length in word_lengths:
    create_similarity_table(cursor, f"similarity_matrix_{length}")

# Retrieve all verses from the database
cursor.execute("SELECT aya_index, text FROM book_quran")
verses = cursor.fetchall()

# Calculate and store similarities for different word lengths
total_verses = len(verses)

# Set a similarity tolerance
tolerance = 0.5

for i in range(total_verses - 1):
    print(f"Processing verse {i + 1}/{total_verses}")

    current_index, current_verse = verses[i]

    for j in range(i + 1, total_verses):
        comp_index, comp_verse = verses[j]

        for length in word_lengths:
            current_words = current_verse.split()[:length]
            comp_words = comp_verse.split()[:length]

            current_text = " ".join(current_words)
            comp_text = " ".join(comp_words)

            similarity_score = calculate_similarity(current_text, comp_text)

            if similarity_score > tolerance:
                cursor.execute(f"INSERT INTO similarity_matrix_{length} VALUES (?, ?, ?, ?)",
                               (current_index, comp_index, similarity_score, length))

                print(f"Aya {current_index} ({current_text}) is similar to Aya {comp_index} ({comp_text}) with a similarity score of {similarity_score} (Word Length: {length})")

    # Commit the changes to the database
    connection.commit()

# Close the database connection
connection.close()
