
# List of comparison strings
comparison_strings = [
    'كسر' ,
    ' ضم',
    'بضم',
    'مكسورة',
    'مشددة',
    'تشديد',
    'ساكنة',
    'مضمومة',
    'فراد',
    'تشديد',
    'تخفيف',
    'مخففة',
    'ممدودة',
    'زيادة',
    'إسكان',
    'بالرفع',
    'بالخفض',
    'مبنيا',
    'فاعله',
    'نون ',
    'نونين ',
    'الجمع',
    'توحيد',
    'تقديم',
    'خطاب',
    'فتحة',
    'سكان',
    'بالياء',
    'بالتاء',
    'بتاء',
    'بياء',
    'بنون',
    'بالنون',
    'فعل',
    'إشمام',
    'بالتوحيد',
    'الجمع',
    'بلا تنوين',
    'بضم',
    'ورفع',
    'وألف بعدها',
    'على التذكير',
    'بياء الغيب',
    'بالنصب',
    'بالرفع',
    'بالنون',
    'بتاء الخطاب',
    'الخطاب',
    'مفتوحة',
    'إسكان',
    'بإسكان',
    'مضمومة',
    'إسكان',
    'مضارع',
    'سكون',
    'منونة',
    'تنوين',
    'التذكير',
    'بحذف',
    'بفتح',
    'بقصر'
    # 'إدغام'
]


# Generate the SQL query dynamically
sql_template = """
----------------------------------------------
SELECT page_number2,sora,aya,sub_subject, reading 
FROM quran_data 
WHERE (
    {conditions}
) 
and ((reading not like 'وقف%') or 
qareesrest not like '%حمزة%')
and ((reading not like 'بالسكت %') or 
qareesrest not like '%حمزة%')
AND (reading <> 'بصلة ميم الجمع وصلا.') 
AND (reading <> 'بصلة ميم الجمع وصلا بخلف.') 
AND (reading <> 'بصلة ميم الجمع وصلا مع الإشباع.') 
AND r5_2 IS NULL 
AND (R6_1 = 1  or R6_2 =1) 
AND r5_2 IS NULL
order by page_number2,sora,aya,id
----------------------------------------------
"""

unique_comparison_strings = list(set(comparison_strings))

# Generate the conditions part of the query with single quotes and commas
conditions_quoted = " OR ".join([f"(reading LIKE '%{comp}%')" for comp in unique_comparison_strings])

# Substitute the conditions into the SQL template
final_sql_query = sql_template.format(conditions=conditions_quoted)

# Print or execute the final SQL query
print(final_sql_query)

# Uncomment the following lines to execute the query using a database connection
# import your_database_module  # Replace with the appropriate database module (e.g., psycopg2, pymysql, sqlite3, etc.)
# connection = your_database_module.connect("your_connection_parameters")
# cursor = connection.cursor()
# cursor.execute(final_sql_query)
# result = cursor.fetchall()
# print(result)
# connection.close()
