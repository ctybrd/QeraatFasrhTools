import sqlite3
import csv
import shutil
import json

# Copy data_v17.db from the source folder to the current folder
source_db_path = r'E:/Qeraat/Wursha_QuranHolder/other/data/data_v17.db'
destination_db_path = 'E:/Qeraat/QeraatFasrhTools/QeraatSearch/data_v17.db'
shutil.copyfile(source_db_path, destination_db_path)

# changed to be here in py 
# Read settings from the JSON file
# with open('./books_settings_simple.json', 'r', encoding='utf-8') as file:
#     settings = json.load(file)

settings=[
    {
        "table_name": "book_asbhni",
        "sql": """SELECT  aya_index, sub_subject ,  ''  subqaree, reading FROM quran_data_tayba WHERE 
        ((qareesrest like '%الأصبهاني%'
        )
        or
        (qareesrest like '%ورش%'
        and qareesrest not like '%أزرق%'
        )
        or
        (qareesrest like '%نافع%'

        and qareesrest not like '%قالون%'
        and qareesrest not like '%أزرق%'
        ))
        and qareesrest not like '%حفص عن عاصم%'

        and (1 = 1) ORDER BY aya_index, id;""",
        "filtering_conditions": [
            "reading<>'بترك هاء السكت وقفا.'",
            "reading<>'بترك السكت، مع تحقيق الهمزة وصلاً ووقفا.'",
            "reading<>'بفتح هاء التأنيث وقفا.'",
            "reading<>'بالفتح في الحالين.'",
            "reading<>'بإسكان ميم الجمع، وترك الصلة.'",
            "reading<>'بتحقيق الهمزة وصلاً ووقفا.'",
            "reading<>'ببقاء غنة النون المدَغمة بخلف.'",
            "reading<>'بالإظهار.'",
            "reading<>'بإدغام النون مع الغنة.'",
            "reading<>'بكسر هاء الضمير وصلاً ووقفا.'",
            "reading<>'بترك السكت على حروف الهجاء في فواتح السور.'",
            "reading<>'بالفتح وقفا.'",
            "reading<>'بترك السكت، مع تحقيق الهمزة.'",
            "reading<>'بقصر الصلة، مع ترك الإدغام.'",
            "reading <>'بترقيق اللام.'",
            "reading<>'بقصر المد في ( لا) النافية للجنس؛ لأن السبب فيها معنوي.'",
            "reading <>'بتحقيق الهمزة مع ترك السكت على المد وصلاً ووقفا.'",
            "reading <>'بتحقيق الهمزة، مع ترك السكت وصلاً ووقفا, .'",
            "reading <>'بتفخيم الراء.'",
            "reading <>'بالفتح وصلاً ووقفا.'",
            "reading <>'بقصر مد البدل.'",
            "reading <> 'بالكسرة الخالصة.'",
            "(sub_subject not like '%صراط%')",
            "reading <>'بتحقيق الهمزة، مع ترك السكت وصلاً ووقفا.'",
            "reading <>'بتحقيق الهمزة في الحالين.'",
            "reading <>'بتحقيق الهمزة، مع ترك السكت على المد وصلاً ووقفا.'",
            "reading <>'بتفخيم الراء، وترك هاء السكت.'",
            "reading<>'قرؤوابالفتح مع تحقيق الهمزة مع ترك السكت على المد وصلاً ووقفا.'",
            "reading <>'بالفتح، مع ترك هاء السكت.'",
            "sub_subject not in('وهو','فهو','لهو','وهو','فهي','لهي','فهي','وهي','ثم هو')",
            "reading <>'بتحقيق الهمزة، مع قصر مد البدل، وبلا هاء السكت.'",
            "reading <>'بترك الإمالة، مع قصر مد البدل.'",
            "readinG<>'بالفتح، مع ترك هاء السكت وقفا.'",
            "readinG<>'بترك الصلة مع قصر الهاء.'",
            "reading<>'بالفتح، مع ترك السكت على المد.'",
            "reading<>'بالفتح، مع تحقيق الهمزة.'",
            "readinG<>'بتحقيق الهمزة، مع ترك السكت، وقصر اللين.'",
            "readinG<>'بضم الهاء وصلاً ووقفا.'",
            "reading <>'بالفتح وقفاً، مع ترقيق اللام.'",
            "reading <>'بتحقيق الهمزة، مع قصر البدل.'",
            "reading <>'بتحقيق الهمزة، مع ترك السكت، وفتح هاء التأنيث.'",
            "reading<>'بتحقيق الهمزتين مع ترك السكت في الحالين.'"
        ]
    },
]
# settings=[
#     {
#         "table_name": "book_all10_t",
#         "sql": "SELECT aya_index, sub_subject || case when count_words =1 then '' when count_words =2 THEN ' (معا)' else '  (جميعا)' end as sub_subject,  readingresult, '' as subqaree, reading FROM quran_data WHERE (1 = 1) ORDER BY aya_index, id;",
#         "filtering_conditions": [
#         ]
#     },
# ]
replacements = {
        'book_common': [

        ]
      }


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

    # Insert data into the table
    insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?' for _ in range(len(data[0]))])})"
    cursor1.executemany(insert_query, data)

    # Commit changes
    conn.commit()

# Function to process result and apply string manipulation
def process_result(result, table_name):
    processed_result = {}
    

    for row in result:
        aya_index, sub_subject, subqaree, reading = row

        #Apply common replacements
        for replacement in replacements['book_common']:
                reading = reading.replace(replacement[0], replacement[1])

        # Apply string replacements based on table_name
        if table_name in replacements:
            for replacement in replacements[table_name]:
                reading = reading.replace(replacement[0], replacement[1])

        #prepare line for aya
        # if readingresult is not None:
        #     processed_text = f'<b>{sub_subject} - {readingresult}</b>: {subqaree}{reading.strip()}'
        # else:
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
conn_data_v17 = sqlite3.connect('E:/Qeraat/QeraatFasrhTools/QeraatSearch/data_v17.db')
db_path = "E:/Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db"
connection = sqlite3.connect(db_path)
cursor = connection.cursor()
columns = 'aya_index INTEGER, text TEXT'
# Loop through ssqls
for setting in settings:
    table_name = setting['table_name']
    sql = setting['sql']
    # Dynamically build the WHERE clause for filtering conditions
    filtering_conditions = setting.get('filtering_conditions', [])
    # #لحذف الكلمات المكررة في نفس الآية
    # filtering_conditions += ['sub_sno =1',]

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
    csv_filename = f'E:/Qeraat/QeraatFasrhTools/QeraatSearch/books/{table_name}.csv'
    export_to_csv(processed_result, csv_filename)

    if processed_result:
        # Create and insert table using processed_result
        create_and_insert_table(conn_data_v17, table_name, columns, processed_result)
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
conn_data_v17.close()
connection.close()
