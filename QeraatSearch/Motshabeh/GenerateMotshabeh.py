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
db_path = r'E:/Qeraat/QeraatFasrhTools/QeraatSearch/Motshabeh/motshabeh.db'
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
tolerance = 0.3

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
#example query
sql1="""
create view Motashabehat1 as SELECT
    sm.index1,
    sm.index2,
    s1.sora_name AS sora_name1,
    b1.aya AS aya1,
    replace(b1.text,'بسم الله الرحمن الرحيم','') AS text1,
    s2.sora_name AS sora_name2,
    b2.aya AS aya2,
    replace(b2.text,'بسم الله الرحمن الرحيم','') AS text2,
    (sm.similarity_score * 100) AS percent_rank
FROM
    similarity_matrix sm
JOIN
    book_quran b1 ON sm.index1 = b1.aya_index
JOIN
    book_quran b2 ON sm.index2 = b2.aya_index
JOIN
    quran_sora s1 ON b1.sora = s1.sora
JOIN
    quran_sora s2 ON b2.sora = s2.sora
WHERE
    b1.text not like '%بسم الله الرحمن الرحيم%'
	and b2.text <>'%الرحمن%';
"""
print(sql1)

sql1= """SELECT
    sm.index1,
    sm.index2,
    s1.sora_name AS sora_name1,
    b1.aya AS aya1,
    replace(b1.text,'بسم الله الرحمن الرحيم','') AS text1,
    s2.sora_name AS sora_name2,
    b2.aya AS aya2,
    replace(b2.text,'بسم الله الرحمن الرحيم','') AS text2,
    (sm.similarity_score * 100) AS percent_rank
FROM
    similarity_matrix sm
JOIN
    book_quran b1 ON sm.index1 = b1.aya_index
JOIN
    book_quran b2 ON sm.index2 = b2.aya_index
JOIN
    quran_sora s1 ON b1.sora = s1.sora
JOIN
    quran_sora s2 ON b2.sora = s2.sora
WHERE
    b1.text not like '%بسم الله الرحمن الرحيم%'
	and b2.text <>'%الرحمن%'
Union
SELECT
    sm.index2 as index1,
    sm.index1 as index2,
    s2.sora_name AS sora_name1,
    b2.aya AS aya1,
    replace(b2.text,'بسم الله الرحمن الرحيم','') AS text1,
    s1.sora_name AS sora_name2,
    b1.aya AS aya2,
    replace(b1.text,'بسم الله الرحمن الرحيم','') AS text2,
    (sm.similarity_score * 100) AS percent_rank
FROM
    similarity_matrix sm
JOIN
    book_quran b1 ON sm.index1 = b1.aya_index
JOIN
    book_quran b2 ON sm.index2 = b2.aya_index
JOIN
    quran_sora s1 ON b1.sora = s1.sora
JOIN
    quran_sora s2 ON b2.sora = s2.sora
WHERE
    b1.text not like '%بسم الله الرحمن الرحيم%'
	and b2.text <>'%الرحمن%'
order by index1

"""
print(sql1)
sql1="""select index1 as aya_index,group_concat(
'<b>' || sora_name2 || ' ' || aya2 || '</b>' || text2 ||' ') as text 
 from MotshabehatU
 group by index1
 order by index1"""
print(sql1)
sql1="""select sora_name1 || ' ' || aya1 || ' ' || text1  as aya1,group_concat(
 sora_name2 || ' ' || aya2 || ' '|| text2 ||' ') as text 
 from MotshabehatU
 group by index1
 order by index1"""
