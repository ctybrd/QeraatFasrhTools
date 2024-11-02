import pandas as pd
import re

# Define a function to remove Arabic diacritics
def remove_diacritics(text):
    if isinstance(text, str):
        # Define diacritic characters to remove
        diacritics_pattern = re.compile(r"[\u0617-\u061A\u064B-\u0652\u0670\u06D6-\u06ED]")
        # Remove diacritics
        return re.sub(diacritics_pattern, '', text)
    return text

# Load the CSV file
input_file = 'E:/Qeraat/QeraatFasrhTools_Data/book_zadmaseer.csv'  # Replace with your file path
output_file = 'E:/Qeraat/QeraatFasrhTools_Data/book_zadmaseer1.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Apply the function to each cell
df = df.applymap(remove_diacritics)

# Save the cleaned data to a new CSV file
df.to_csv(output_file, index=False)

print("Diacritics removed and file saved as", output_file)
