import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('e:/qeraat/data_v15.db')
cursor = conn.cursor()

# Execute the query to retrieve data from both tables
query = '''
SELECT mj.text, ms.page_number
FROM book_jlalin AS mj
JOIN mosshf_shmrly AS ms ON mj.aya_index = ms.aya_index
'''
cursor.execute(query)
data = cursor.fetchall()

# Create a dictionary to store the Ayas for each page
pages = {}

# Iterate over the retrieved data
for text, page_number in data:
    # Check if the page number already exists in the dictionary
    if page_number in pages:
        # Concatenate the text for the current page
        pages[page_number]['text'] += f'<p>{text}</p>'
    else:
        # Create a new entry for the page
        pages[page_number] = {'text': f'<p>{text}</p>'}

# Generate the HTML content
html_content = ''

# Iterate over the pages
for page_number, page_data in pages.items():
    # Construct the image path
    image_path = f'E:/Qeraat/pages/{page_number}.jpg'  # Replace with the actual image path format

    # Wrap the image and text in a container div
    html_content += f'<div style="clear:both;">' \
                    f'<img src="{image_path}" style="float:right;width:200px;height:200px;margin-left:10px;">' \
                    f'{page_data["text"]}' \
                    f'</div>'

# Generate the HTML document
html = f'''
<html>
<head>
<title>Page Content</title>
</head>
<body>
{html_content}
</body>
</html>
'''

# Save the HTML file
with open('output.html', 'w', encoding='utf-8') as file:
    file.write(html)

# Close the database connection
conn.close()
