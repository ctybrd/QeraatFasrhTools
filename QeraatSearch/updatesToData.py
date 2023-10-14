import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('E:/Qeraat/QeraatFasrhTools_Data/nquran_data.db')
cursor = conn.cursor()
cursor.execute("update quran_data set R5_2=Null where R5_2=0")
conn.commit()
cursor.execute("update quran_data set Q5=Null where Q5=0")
conn.commit()
for col_num in range(1, 11):
    cursor.execute(f"UPDATE quran_data SET Q{col_num} = NULL WHERE R{col_num}_1 IS NULL OR R{col_num}_2 IS NULL")

# Commit the changes for the additional updates
conn.commit()
# Close the database connection
conn.close()
