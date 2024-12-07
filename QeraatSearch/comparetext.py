import re
import unicodedata
import pyarabic.araby as araby

# File paths
file1_path = r"D:\temp\quran_txt.txt"
file2_path = r"D:\temp\quran_txt_new.txt"
output_path = r"D:\temp\differences.txt"

# Function to preprocess and normalize text
def preprocess_text(text):
    # Remove diacritics using pyarabic
    text = araby.strip_diacritics(text)
    # Normalize Unicode (NFKC handles canonical and compatibility forms)
    text = unicodedata.normalize('NFKC', text)
    # Remove Arabic numerals
    text = re.sub(r'[٠-٩]', '', text)
    text = re.sub(r'۩', '', text)
    text = re.sub(r'۞', '', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Strip leading and trailing spaces
    return text.strip()

# Read and preprocess files
with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
    text1 = preprocess_text(file1.read())
    text2 = preprocess_text(file2.read())

# Split into words
words1 = text1.split()
words2 = text2.split()

# Find differences
diffs = []
for i, (word1, word2) in enumerate(zip(words1, words2)):
    if word1 != word2:
        diffs.append(f"Word {i + 1}: '{word1}' (file1) vs '{word2}' (file2)")

# Include additional words if files are of different lengths
if len(words1) > len(words2):
    diffs.extend([f"Word {i + 1}: '{word}' (file1) vs None (file2)" for i, word in enumerate(words1[len(words2):], start=len(words2))])
elif len(words2) > len(words1):
    diffs.extend([f"Word {i + 1}: None (file1) vs '{word}' (file2)" for i, word in enumerate(words2[len(words1):], start=len(words1))])

# Write differences to file
with open(output_path, 'w', encoding='utf-8') as output_file:
    if diffs:
        output_file.write("Differences found:\n")
        output_file.write("\n".join(diffs))
    else:
        output_file.write("The files are identical.")

print(f"Differences have been saved to: {output_path}")
