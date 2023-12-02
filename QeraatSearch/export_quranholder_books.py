import sqlite3
import csv
import shutil
import json

# Copy data_v17.db from the source folder to the current folder
source_db_path = r'E:/Qeraat/Wursha_QuranHolder/other/data/data_v17.db'
destination_db_path = './data_v17.db'
shutil.copyfile(source_db_path, destination_db_path)

# Function to execute a query and return the result
def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

# Function to export data to CSV
def export_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)

# Function to create a new table in the data_v17.db database and insert data into it
def create_and_insert_table(conn, table_name, columns, data):
    cursor = conn.cursor()

    # Drop table if exists
    drop_table_query = f"DROP TABLE IF EXISTS {table_name}"
    cursor.execute(drop_table_query)

    # Create table
    create_table_query = f"CREATE TABLE {table_name} ({columns})"
    cursor.execute(create_table_query)

    # Insert data into the table
    insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?' for _ in range(len(data[0]))])})"
    cursor.executemany(insert_query, data)

    # Commit changes
    conn.commit()

# Connect to the databases
conn_data_v17 = sqlite3.connect('./data_v17.db')
db_path = "./qeraat_data.db"
connection = sqlite3.connect(db_path)
cursor = connection.cursor()
columns = 'aya_index INTEGER, text TEXT'

# Read settings from the JSON file
with open('./books_settings.json', 'r', encoding='utf-8') as file:
    settings = json.load(file)

# Loop through settings
for setting in settings:
    table_name = setting['table_name']
    sql = setting['sql']
    print(sql)
    # Execute the SQL query
    cursor.execute(sql)
    result = cursor.fetchall()

    # Export to CSV
    csv_filename = f'./books/{table_name}.csv'
    export_to_csv(result, csv_filename)

    if result:
      create_and_insert_table(conn_data_v17, table_name, columns, result)
    else:
      print("failed "+table_name)
# Close connections
conn_data_v17.close()
connection.close()
