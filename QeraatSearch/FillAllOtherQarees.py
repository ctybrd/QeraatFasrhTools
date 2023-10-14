import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('E:/Qeraat/QeraatFasrhTools_Data/nquran_data.db')
cursor = conn.cursor()

# Query the rows ordered by aya_index
cursor.execute("SELECT * FROM quran_data where sora =1 ORDER BY aya_index,id")
rows = cursor.fetchall()

# Define the column names based on your specific naming convention
q_and_r_column_names = ['Q1', 'R1_1', 'R1_2', 'Q2', 'R2_1', 'R2_2', 'Q3', 'R3_1', 'R3_2', 'Q4', 'R4_1', 'R4_2', 'Q5', 'R5_1', 'R5_2', 'Q6', 'R6_1', 'R6_2', 'Q7', 'R7_1', 'R7_2', 'Q8', 'R8_1', 'R8_2', 'Q9', 'R9_1', 'R9_2', 'Q10', 'R10_1', 'R10_2']

# Initialize variables to keep track of the current group
current_group = []
last_aya_index = None
filled_columns = set()  # To keep track of columns that were filled

for row in rows:
    aya_index = row[0]
    qarees = row[5]
    if  aya_index != last_aya_index:
            filled_columns = set()  # Reset the filled columns for the new group

    if qarees == 'باقي الرواة':
        # Group boundary reached, build a single UPDATE statement for the complement columns
        complement_columns = ', '.join([f"{col} = '1'" for col in q_and_r_column_names if col not in filled_columns])
        if complement_columns:
            update_query = f"UPDATE quran_data SET {complement_columns} WHERE id = {row[1]} AND aya_index = {aya_index}"
            cursor.execute(update_query)
            print(f"Filled {aya_index}:{complement_columns} for aya_index = {aya_index}")
        filled_columns = set()  # Reset the filled columns for the new group

    if qarees != 'باقي الرواة' :
        # Track which columns are filled in this row
        for col_name in q_and_r_column_names:
            if  row[q_and_r_column_names.index(col_name) + 9]=='1':
                filled_columns.add(col_name)
                print(f"Marked {aya_index}: {col_name} as filled for aya_index = {aya_index}")

    last_aya_index = aya_index

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
