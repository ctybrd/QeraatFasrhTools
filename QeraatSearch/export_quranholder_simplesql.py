import sqlite3
import csv
import shutil
import json
import os
# Copy data_v17.db from the source folder to the current folder
script_path = os.path.abspath(__file__)
drive, _ = os.path.splitdrive(script_path) 
drive = drive +'/'

source_db_path = drive + r'Qeraat/Wursha_QuranHolder/other/data/data_v19.db'
destination_db_path = drive +  r'Qeraat/QeraatFasrhTools/QeraatSearch/data_v19.db'
shutil.copyfile(source_db_path, destination_db_path)

# changed to be here in py 
# Read settings from the JSON file
# with open('./books_settings_simple.json', 'r', encoding='utf-8') as file:
#     settings = json.load(file)

settings=[

    {
        "table_name": "book_qqalon",
        "sql": "SELECT aya_index, sub_subject || case when count_words =1 then '' when count_words =2 THEN ' (معا)' else '  (جميعا)' end as sub_subject,  resultnew, '' as subqaree, reading FROM quran_data WHERE  (1 = 1)  ORDER BY aya_index, id;",
        "filtering_conditions": [
            " R1_1 IS NOT NULL ",
            " IFNULL(r5_2, 0) = 0 ",
            " IFNULL(tags, '') NOT LIKE '%basmala%' ",
            " reading NOT LIKE 'قرأ بصلة ميم الجمع وصل%' "
        ]
    },
    {
        "table_name": "book_qwarsh",
        "sql": "SELECT aya_index, sub_subject || case when count_words =1 then '' when count_words =2 THEN ' (معا)' else '  (جميعا)' end as sub_subject,  resultnew, '' as subqaree, reading FROM quran_data WHERE (1 = 1) ORDER BY aya_index, id;",
        "filtering_conditions": [
            " R1_2 IS NOT NULL ",
            " IFNULL(r5_2, 0) = 0 ",
            " IFNULL(tags, '') NOT LIKE '%basmala%' "
        ]
    },
    {
        "table_name": "book_qibnkather",
        "sql": "SELECT aya_index, sub_subject || case when count_words =1 then '' when count_words =2 THEN ' (معا)' else '  (جميعا)' end as sub_subject,  resultnew, CASE WHEN q2 IS NOT NULL THEN '' ELSE CASE WHEN r2_1 IS NOT NULL THEN 'البزي ' ELSE 'قنبل ' END END as subqaree, reading FROM quran_data WHERE (1 = 1) ORDER BY aya_index, id;",
        "filtering_conditions": [
            " (R2_1 IS NOT NULL or R2_2 IS NOT NULL) " ,
            " IFNULL(r5_2, 0) = 0 ",
            " IFNULL(tags, '') NOT LIKE '%basmala%' ",
            " reading <> 'بصلة ميم الجمع وصلا.' ",
            " reading <> 'بضم ميم الجمع، ووصلها بواو لفظية.' ",
        ]
    },
    {
        "table_name": "book_aboamro",
        "sql": "SELECT aya_index, sub_subject || case when count_words =1 then '' when count_words =2 THEN ' (معا)' else '  (جميعا)' end as sub_subject,  resultnew, CASE WHEN q3 IS NOT NULL THEN '' ELSE CASE WHEN r3_1 IS NOT NULL THEN 'الدوري ' ELSE 'السوسي ' END END as subqaree, reading FROM quran_data WHERE (1 = 1) ORDER BY aya_index, id;",
        "filtering_conditions": [
            " (R3_1 IS NOT NULL or R3_2 IS NOT NULL) " ,
            " IFNULL(r5_2, 0) = 0 ",
            " IFNULL(tags, '') NOT LIKE '%basmala%' "
        ]
    },
    {
        "table_name": "book_ibnamer",
        "sql": "SELECT aya_index, sub_subject || case when count_words =1 then '' when count_words =2 THEN ' (معا)' else '  (جميعا)' end as sub_subject,  resultnew, CASE WHEN q4 IS NOT NULL THEN '' ELSE CASE WHEN r4_1 IS NOT NULL THEN 'هشام ' ELSE 'ابن ذكوان ' END END as subqaree, reading FROM quran_data WHERE (1 = 1) ORDER BY aya_index, id;",
        "filtering_conditions": [
            " (R4_1 IS NOT NULL or R4_2 IS NOT NULL) " ,
            " IFNULL(r5_2, 0) = 0 ",
            " IFNULL(tags, '') NOT LIKE '%basmala%' "
        ]
    },
    {
        "table_name": "book_sho3ba",
        "sql": "SELECT aya_index, sub_subject || case when count_words =1 then '' when count_words =2 THEN ' (معا)' else '  (جميعا)' end as sub_subject,  resultnew, '' as subqaree, reading FROM quran_data WHERE (1 = 1) ORDER BY aya_index, id;",
        "filtering_conditions": [
            " R5_1 IS NOT NULL " ,
            " IFNULL(r5_2, 0) = 0 ",
            " IFNULL(tags, '') NOT LIKE '%basmala%' "
        ]
    },
    {
        "table_name": "book_qhamza",
        "sql": "SELECT aya_index, sub_subject || case when count_words =1 then '' when count_words =2 THEN ' (معا)' else '  (جميعا)' end as sub_subject,  resultnew, CASE WHEN q6 IS NOT NULL THEN '' ELSE CASE WHEN r6_1 IS NOT NULL THEN 'خلف ' ELSE 'خلاد ' END END as subqaree, reading FROM quran_data WHERE (1 = 1) ORDER BY aya_index, id;",
        "filtering_conditions": [
            " qareesrest LIKE '%حمزة%' ",
            " IFNULL(r5_2, 0) = 0 ",
            " IFNULL(tags, '') NOT LIKE '%basmala%' "
        ]
    },
    {
        "table_name": "book_kisai",
        "sql": "SELECT aya_index, sub_subject || case when count_words =1 then '' when count_words =2 THEN ' (معا)' else '  (جميعا)' end as sub_subject,  resultnew, CASE WHEN q7 IS NOT NULL THEN '' ELSE CASE WHEN r7_1 IS NOT NULL THEN 'أبوالحارث ' ELSE 'الدوري ' END END as subqaree, reading FROM quran_data WHERE (1 = 1) ORDER BY aya_index, id;",
        "filtering_conditions": [
            " (R7_1 IS NOT NULL or R7_2 IS NOT NULL) " ,
            " IFNULL(r5_2, 0) = 0 ",
            " IFNULL(tags, '') NOT LIKE '%basmala%' "
        ]
    },
    {
        "table_name": "book_abujafar",
        "sql": "SELECT aya_index, sub_subject || case when count_words =1 then '' when count_words =2 THEN ' (معا)' else '  (جميعا)' end as sub_subject,  resultnew, CASE WHEN q8 IS NOT NULL THEN '' ELSE CASE WHEN r8_1 IS NOT NULL THEN 'ابن وردان ' ELSE 'ابن جماز ' END END as subqaree, reading FROM quran_data WHERE (1 = 1) ORDER BY aya_index, id;",
        "filtering_conditions": [
            " (R8_1 IS NOT NULL or R8_2 IS NOT NULL) " ,
            " IFNULL(r5_2, 0) = 0 ",
            " IFNULL(tags, '') NOT LIKE '%basmala%' ",
            " reading <> 'بصلة ميم الجمع وصلا.' ",
            " reading <> 'بضم ميم الجمع، ووصلها بواو لفظية.' ",
        ]
    },
    {
        "table_name": "book_yaqob",
        "sql": "SELECT aya_index, sub_subject || case when count_words =1 then '' when count_words =2 THEN ' (معا)' else '  (جميعا)' end as sub_subject,  resultnew, CASE WHEN q9 IS NOT NULL THEN '' ELSE CASE WHEN r9_1 IS NOT NULL THEN 'رويس ' ELSE 'روح ' END END as subqaree, reading FROM quran_data WHERE (1 = 1) ORDER BY aya_index, id;",
        "filtering_conditions": [
            " (R9_1 IS NOT NULL or R9_2 IS NOT NULL) " ,
            " IFNULL(r5_2, 0) = 0 ",
            " IFNULL(tags, '') NOT LIKE '%basmala%' ",       
        ]
    },
    {
        "table_name": "book_khalaf",
        "sql": "SELECT aya_index, sub_subject || case when count_words =1 then '' when count_words =2 THEN ' (معا)' else '  (جميعا)' end as sub_subject,  resultnew, CASE WHEN q10 IS NOT NULL THEN '' ELSE CASE WHEN r10_1 IS NOT NULL THEN 'إسحق ' ELSE 'إدريس ' END END as subqaree, reading FROM quran_data WHERE (1 = 1) ORDER BY aya_index, id;",
        "filtering_conditions": [
            " (R10_1 IS NOT NULL or R10_2 IS NOT NULL) " ,
            " IFNULL(r5_2, 0) = 0 ",
            " IFNULL(tags, '') NOT LIKE '%basmala%' ",       
        ]
    },
    {
        "table_name": "book_all10",
        "sql": "SELECT aya_index, sub_subject || case when count_words =1 then '' when count_words =2 THEN ' (معا)' else '  (جميعا)' end as sub_subject,  resultnew, qareesrest  || '  ' as subqaree, reading FROM quran_data WHERE (1 = 1) ORDER BY aya_index, id;",
        "filtering_conditions": [
        "reading <> 'قرؤوا بفتح هاء التأنيث.'",
        "reading <> 'وقف بترك هاء السكت.'",
        "reading <> 'قرؤوا بترك صلة ميم الجمع.'",
        "Not ((reading like '%بتحقيق الهمز%') and (qarees='باقي الرواة'))",
        "Not ((reading like '%بتحقيق الهمز%') and (qarees='قرؤوا بترك السكت مع تحقيق الهمزة وصلاً ووقفا.'))",
        "Not ((reading like '%بتحقيق الهمز%') and (qarees='قرؤوا بترك السكت، وإسكان ميم الجمع وصلاً ووقفا.'))"
        ]
    },

  
]
# Define string replacements based on table_name
            # ('قرأ', ''),
            # ('قرؤوا', ''),
            # ('بلا خلاف عنه', ''),
            # ('حرفا مديا من جنس حركة ما قبلها', ''),
            # ('بالنقل وصلاً ووقفا','بالنقل'),
            # ('خلافا لجمهور القراء','')
replacements = {
        'book_common': [

        ],
        'book_qqalon': [

        ],
        'book_qhamza': [
  
        ],
        'book_qwarsh': [
        ],
        'book_qibnkather': [

        ]
      }

# Function to execute a query and return the result
# def execute_query(cursor, query):
#     cursor.execute(query)
#     return cursor.fetchall()

# Function to export data to CSV
def export_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)

# Function to create a new table in the data_v17.db database and insert data into it
def create_and_insert_table(conn, table_name, columns, data):
    cursor1 = conn.cursor()

    # Drop table if exists
    drop_table_query = f"DROP TABLE IF EXISTS {table_name}"
    cursor1.execute(drop_table_query)

    # Create table
    create_table_query = f"CREATE TABLE {table_name} ({columns})"
    cursor1.execute(create_table_query)

    # Define the Arabic tatweel character
    tatweel = "ـ"

    # Create a new list where the tatweel character is removed from all strings
    cleaned_data = [
        [item.replace(tatweel, "") if isinstance(item, str) else item for item in row] 
        for row in data
    ]

    # Prepare the insert query
    insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?' for _ in range(len(cleaned_data[0]))])})"

    # Execute the insert with the cleaned data
    cursor1.executemany(insert_query, cleaned_data)




    # Commit changes
    conn.commit()

# Function to process result and apply string manipulation
def process_result(result, table_name):
    processed_result = {}
    

    for row in result:
        aya_index, sub_subject,  resultnew, subqaree, reading = row

        #Apply common replacements
        for replacement in replacements['book_common']:
                reading = reading.replace(replacement[0], replacement[1])

        # Apply string replacements based on table_name
        if table_name in replacements:
            for replacement in replacements[table_name]:
                reading = reading.replace(replacement[0], replacement[1])

        #prepare line for aya
        if resultnew is not None:
            processed_text = f'<b>{sub_subject} - {resultnew}</b>: {subqaree}{reading.strip()}'
        else:
            processed_text = f'<b>{sub_subject}</b>: {subqaree}{reading.strip()}'
        
        # Append to the existing text for the same aya_index or create a new entry
        if aya_index in processed_result:
            processed_result[aya_index].append(processed_text)
        else:
            processed_result[aya_index] = [processed_text]

    # Convert the dictionary to a list of tuples
    final_result = [(key, ' '.join(value)) for key, value in processed_result.items()]
    return final_result



# Connect to the databases
conn_data_v18 = sqlite3.connect(drive + 'Qeraat/QeraatFasrhTools/QeraatSearch/data_v19.db')
db_path = drive +"Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db"
connection = sqlite3.connect(db_path)
cursor = connection.cursor()
columns = 'aya_index INTEGER, text TEXT'
# Loop through ssqls
for setting in settings:
    table_name = setting['table_name']
    sql = setting['sql']
    # Dynamically build the WHERE clause for filtering conditions
    filtering_conditions = setting.get('filtering_conditions', [])
    #لحذف الكلمات المكررة في نفس الآية
    filtering_conditions += ['sub_sno =1',]

    if '(1 = 1)' in sql:
        where_clause = " AND ".join(filtering_conditions)
        if where_clause:
          sql = sql.replace('(1 = 1)', f'({where_clause})', 1)
            
    # Execute the SQL query
    print(sql,table_name)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    processed_result = process_result(result,table_name)
    
    # Export to CSV using processed_result
    csv_filename = drive+f'Qeraat/QeraatFasrhTools/QeraatSearch/books/{table_name}.csv'
    export_to_csv(processed_result, csv_filename)

    if processed_result:
        # Create and insert table using processed_result
        create_and_insert_table(conn_data_v18, table_name, columns, processed_result)
    else:
        print("failed " + table_name)
#prepare view
view_sql=''
for table_setting in settings:
    table_name = table_setting["table_name"]
    print(table_name)
    # subquery_sql = f"(SELECT text FROM {table_name} WHERE aya_index = mosshf_shmrly.aya_index) AS {table_name.lower()},\n"
    # view_sql += subquery_sql
print(view_sql)
# Close connections
conn_data_v18.close()
connection.close()
