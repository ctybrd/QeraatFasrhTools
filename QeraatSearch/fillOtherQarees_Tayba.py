import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('E:/Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db')
cursor = conn.cursor()

# Query the rows ordered by aya_index
cursor.execute("SELECT * FROM quran_data_tayba where qarees <>'كل الرواة' ORDER BY aya_index,id")
rows = cursor.fetchall()

# Define the column names based on your specific naming convention

# Initialize variables to keep track of the current group

last_aya_index = None
filled_columns = set()  # To keep track of columns that were filled

for row in rows:
    aya_index = row[0]
    qarees = row[5]
    print(f"{aya_index}")
    if  aya_index != last_aya_index:
            filled_columns = ''  # #set() Reset the filled columns for the new group

    if qarees == 'الباقون':
        if 'الأصبهاني' not in filled_columns:
            update_query = f"UPDATE quran_data SET qareesrest='الأصبهاني عن ورش عن نافع' WHERE id = {row[1]} AND aya_index = {aya_index}"
            cursor.execute(update_query)
        # print(f"Filled {aya_index}:{complement_columns} for aya_index = {aya_index}")
        filled_columns = ''  #set()  # Reset the filled columns for the new group

    if qarees != 'الباقون' :
        # Track which columns are filled in this row
        filled_columns += qarees
        # print(f"Marked {aya_index}: {col_name} as filled for aya_index = {aya_index}")

    last_aya_index = aya_index

# Commit the changes to the database
conn.commit()
# Close the database connection
conn.close()
