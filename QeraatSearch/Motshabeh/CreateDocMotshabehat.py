import sqlite3
from docx import Document
from docx.shared import RGBColor
from difflib import unified_diff

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
    diff = unified_diff(text1.splitlines(), text2.splitlines())
    result = '\n'.join(list(diff)[2:])  # Skip the diff header

    for line in result.split('\n'):
        if line.startswith('- '):
            yield ('delete', line[2:])
        elif line.startswith('+ '):
            yield ('insert', line[2:])
        else:
            yield ('common', line)

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

    # Grouping information
    doc.add_paragraph(f"Sora_name1: {sora_name1}, Aya1: {aya1}")
    doc.add_paragraph(f"Sora_name2: {sora_name2}, Aya2: {aya2}")

    # Highlight differences between text1 and text2
    differences = list(highlight_differences(text1, text2))
    add_colored_paragraph(doc, differences)

    # Add a separator line between groups
    doc.add_paragraph("\n" + "=" * 50 + "\n")

# Save the document
doc.save('Motshabehat70.docx')

# Close the database connection
connection.close()
