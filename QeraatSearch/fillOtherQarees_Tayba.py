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
        qfound = ('الأصبهاني' in filled_columns)
        qfound = qfound or ('نافع' in filled_columns and 'قالون عن' not in filled_columns and 'الأزرق' not in filled_columns)
        qfound = qfound or ('ورش' in filled_columns and 'عن ورش' not in filled_columns)
        if not qfound:      
            update_query = f"UPDATE quran_data_tayba SET qareesrest='الأصبهاني عن ورش عن نافع' WHERE id = {row[1]} AND aya_index = {aya_index}"
            cursor.execute(update_query)
            # print(update_query)
        # print(f"Filled {aya_index}:{complement_columns} for aya_index = {aya_index}")
        filled_columns = ''  #set()  # Reset the filled columns for the new group

    if qarees != 'الباقون' :
        # Track which columns are filled in this row
        filled_columns += qarees
        # print(f"Marked {aya_index}: {col_name} as filled for aya_index = {aya_index}")

    last_aya_index = aya_index

# Commit the changes to the database
conn.commit()
update_query = f"UPDATE quran_data_tayba SET qareesrest=qarees where qareesrest is null"
cursor.execute(update_query)
conn.commit()
# Close the database connection
conn.close()
