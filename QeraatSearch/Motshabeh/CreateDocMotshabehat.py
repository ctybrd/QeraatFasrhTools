import sqlite3
from docx import Document
from docx.shared import RGBColor
from difflib import unified_diff
from difflib import ndiff

# Connect to the SQLite database
db_path = "E:/Qeraat/QeraatFasrhTools/QeraatSearch/Motshabeh/motshabeh7.db"
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Execute the query
query = """
    SELECT sora_name1, aya1, text1, sora_name2, aya2, text2
    FROM MotshabehatU
    GROUP BY index1
    ORDER BY index1
"""
cursor.execute(query)
results = cursor.fetchall()

# Create a Word document
doc = Document()

# Function to compare and highlight differences
def highlight_differences(text1, text2):
    diff = ndiff(text1.split(), text2.split())
    result = ' '.join(list(diff))

    for item in result.split():
        if item.startswith('-'):
            yield ('delete', item[1:])
        elif item.startswith('+'):
            yield ('insert', item[1:])
        else:
            yield ('common', item)

# Function to add a paragraph with colored text
def add_colored_paragraph(doc, items):
    paragraph = doc.add_paragraph()
    for item_type, item_text in items:
        run = paragraph.add_run(item_text)
        if item_type == 'delete':
            run.font.color.rgb = RGBColor(255, 0, 0)  # Red for deletions
        elif item_type == 'insert':
            run.font.color.rgb = RGBColor(0, 0, 255)  # Blue for insertions
        # 'common' items will have the default color

# Iterate through the results and add paragraphs to the document
for row in results:
    sora_name1, aya1, text1, sora_name2, aya2, text2 = row

    # Highlight differences between text1 and text2
    differences = list(highlight_differences(text1, text2))
    add_colored_paragraph(doc, differences)

    # Add a separator line between pairs
    doc.add_paragraph("\n" + "=" * 50 + "\n")

# Save the document
doc.save('Motshabehat70.docx')

# Close the database connection
connection.close()
