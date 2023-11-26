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

# Connect to the SQLite database
db_path = r'E:/Qeraat/QeraatFasrhTools/QeraatSearch/motshabeh.db'
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Truncate the similarity table if it exists
cursor.execute("DROP TABLE IF EXISTS similarity_matrix")
connection.commit()

# Create the similarity matrix table
cursor.execute("CREATE TABLE similarity_matrix (index1 INTEGER, index2 INTEGER, similarity_score REAL)")

# Retrieve all verses from the database
cursor.execute("SELECT aya_index, text FROM book_quran")
verses = cursor.fetchall()

# Calculate and store similarities
total_verses = len(verses)

# Set a similarity tolerance
tolerance = 0.7

for i in range(total_verses - 1):  # Start from the first verse and go up to the second-to-last verse
    print(f"Processing verse {i + 1}/{total_verses}")

    current_index, current_verse = verses[i]

    for j in range(i + 1, total_verses):  # Start from the next verse to the end
        comp_index, comp_verse = verses[j]

        similarity_score = calculate_similarity(current_verse, comp_verse)

        # Check if similarity is above the tolerance threshold
        if similarity_score > tolerance:
            # Insert the similarity score into the table
            cursor.execute("INSERT INTO similarity_matrix VALUES (?, ?, ?)", (current_index, comp_index, similarity_score))

            # Print information about the verses being compared
            print(f"Aya {current_index} ({current_verse}) is similar to Aya {comp_index} ({comp_verse}) with a similarity score of {similarity_score}")

# Commit the changes to the database
connection.commit()

# Close the database connection
connection.close()

