import sqlite3
import shutil
import os

# Copy data_v17.db from the source folder to the destination folder
script_path = os.path.abspath(__file__)
drive, _ = os.path.splitdrive(script_path)
drive = drive + '/'

source_db_path = drive + r'Qeraat/Wursha_QuranHolder/other/data/data_v17.db'
destination_db_path = drive + r'Qeraat/QeraatFasrhTools/QeraatSearch/data_v17.db'
shutil.copyfile(source_db_path, destination_db_path)

# List of table names to update
table_names = [
    "book_qqalon",
    "book_qwarsh",
    "book_qibnkather",
    "book_aboamro",
    "book_ibnamer",
    "book_sho3ba",
    "book_qhamza",
    "book_kisai",
    "book_abujafar",
    "book_yaqob",
    "book_khalaf",
    "book_all10"
]

# Connect to the database and update the text in the specified tables
conn_data_v17 = sqlite3.connect(destination_db_path)
cursor1 = conn_data_v17.cursor()
for table in table_names:
    sql = "UPDATE " + table + " SET text = REPLACE(text, 'ـ', '')"
    print(sql)
    cursor1.execute(sql)
    conn_data_v17.commit()
    sql = "UPDATE " + table + " SET text = REPLACE(text, '  ', ' ')"
    print(sql)
    cursor1.execute(sql)
    conn_data_v17.commit()
    sql = "UPDATE " + table + " SET text = REPLACE(text, '  ', ' ')"
    print(sql)
    cursor1.execute(sql)
    conn_data_v17.commit()
    sql = "UPDATE " + table + " SET text = REPLACE(text, '  ', ' ')"
    print(sql)
    cursor1.execute(sql)
    conn_data_v17.commit()
    sql = "UPDATE " + table + " SET text = REPLACE(text, '.', '')"
    print(sql)
    cursor1.execute(sql)
    conn_data_v17.commit()
    sql = "UPDATE " + table + " SET text = REPLACE(text, 'مع قصر مد البدل', '')"
    print(sql)
    cursor1.execute(sql)
    conn_data_v17.commit()
    sql = "UPDATE " + table + " SET text = REPLACE(text,'بالفتح م وقفا'    ,'بالفتح وقفا')"
    print(sql)
    cursor1.execute(sql)
    conn_data_v17.commit()
    sql = "UPDATE " + table + " SET text = REPLACE(text , 'بالفتح م وصلا','بالفتح وصلا')"
    print(sql)
    cursor1.execute(sql)
    conn_data_v17.commit()


# Commit the changes and close the connection
conn_data_v17.commit()
conn_data_v17.close()
