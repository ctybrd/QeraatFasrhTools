import os
import shutil
import zipfile
import pyodbc
import sqlite3
import re
from PyPDF2 import PdfReader

import matplotlib.colors as mcolors
import webcolors

def extract_line_comments(pdf_path):
    #column style (S = solid D =dashed H hollow circle)
    #column circle (empty = line only 1= line with right circle 2 = line with left circle 4 circle only for future use 3 will be center circle of the line )
    comments = []
    pdf = PdfReader(pdf_path)

    for pageno, page in enumerate(pdf.pages):
        #for test
        # if pageno >= 3:
        #      break  # Exit the loop after processing the 7th page
        try:
            annotations = page['/Annots']        
            if annotations:
                for annotation in annotations:
                    if isinstance(annotation, str):
                        annotation = pdf.get_object(annotation)
                    elif isinstance(annotation, dict):
                        annotation = pdf._buildIndirectObject(annotation)
                    # print(annotation.get_object()['/Subtype'])
                    if annotation.get_object()['/Subtype'] == '/Line':
                        comment = {
                            'content': ' ',
                            'pageno': pageno+1,
                            'coordinates': annotation.get_object()['/Rect'],
                            'color': annotation.get_object()['/C']
                        }
                        comment['style'] = 'S'
                        comment['circle'] = ''
                        if '/BS' in annotation.get_object():
                            if '/S' in annotation.get_object()['/BS']:
                                comment['style'] = str(annotation.get_object()['/BS']['/S'])
                        if comment['style']=='/D':
                            comment['style'] = 'D'
                        if '/LE' in annotation.get_object():
                            if(str(annotation.get_object()['/LE'])) == "['/Circle', '/None']":
                                comment['circle'] ='2'
                            elif (str(annotation.get_object()['/LE'])) == "['/None', '/Circle']":
                                comment['circle'] ='1'
                        comments.append(comment)
                        
                    if annotation.get_object()['/Subtype'] == '/Circle':
                        comment = {
                            'content': ' ',
                            'pageno': pageno + 1,
                            'coordinates': annotation.get_object()['/Rect'],
                            'color': annotation.get_object()['/C']
                        }
                        # print(annotation.get_object())
                        comment['style'] = 'S'
                        comment['circle'] = '4'
                        # if '/BS' in annotation.get_object():
                        #     if '/S' in annotation.get_object()['/BS']:
                        #         comment['style'] = str(annotation.get_object()['/BS']['/S'])
                        
                        # Check if the oval fill color is none
                        # if '/MK' in annotation.get_object() and '/BG' in annotation.get_object()['/MK']:
                        if '/IC' in annotation.get_object():
                            fill_color = annotation.get_object()['/IC']
                            if fill_color == '[0 0 0]':
                                comment['style'] = 'H'
                        else:
                            comment['style'] = 'H'
                        
                        comments.append(comment)
                    

                        
        except Exception as e:
            # print(f"Error processing annotations on page {pageno}: {e}")
            pass


    return comments


def create_table_sqlite():
    conn = sqlite3.connect('E:/Qeraat/farsh_v6.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS shmrly
                 (qaree TEXT, page_number INTEGER, color TEXT, type NUMERIC, x REAL, y REAL, width REAL)''')
    conn.commit()
    conn.close()

"""
Circle Column Specification:
- '1' indicates a circle at the right edge of the line.
- '2' indicates a circle at the left edge of the line.
- '4' indicates only a circle (no line).

Style Column Specification:
- 'D' indicates a dashed line.
- 'S' indicates a solid line and filled circle (only applicable when '4' is present in circle).
- 'H' indicates a solid line and hollow circle (only applicable when '4' is present in circle).
"""


def insert_comments_sqlite(comments,qaree_key):
    conn = sqlite3.connect('E:/Qeraat/farsh_v6.db')
    c = conn.cursor()
    # Delete rows with value "A" in the field "qaree"
    c.execute("DELETE FROM shmrly WHERE qaree = ?", (qaree_key,))
    if qaree_key == "A":
        c.execute("DELETE FROM shmrly WHERE (qaree = 'W') and ((color in ('blue','olive')) or (circle = '4'))")
        # c.execute("DELETE FROM shmrly WHERE qaree = 'W' and Circle='4'") #AYA COUNT MARKS
        c.execute("DELETE FROM shmrly WHERE qaree = 'K' and Circle='4'")
    if qaree_key == "I":
        c.execute("DELETE FROM shmrly WHERE qaree = 'H'") # Hesham is subset of ibnamer
        c.execute("DELETE FROM shmrly WHERE qaree = 'Z'") # Ibn thakwan is a subset of ibnamer


    if qaree_key == 'T':
        xshift = 70.0  
    else:
        xshift = 81.0
    
    for comment in comments:
        # print(comment['content'], comment['coordinates'], comment['color'])

        coordinates = str(comment['coordinates'])
        matches = re.findall(r'(\d+\.?\d*)', coordinates)
        x1, y1, x2, y2 = matches

        color_values = get_color_name(str(comment['color']),qaree_key)
        if qaree_key != 'T':
            color_type = get_color_type(color_values)
        else:
            color_type = 'Tayseer'
        c.execute("INSERT INTO shmrly(qaree, page_number, color, type, x, y, width,style,circle) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (qaree_key, comment['pageno'], str(color_values), str(color_type), float((float(x1)-xshift)/443.0), 1-(float((float(y1)-81.0)/691.0)),max(0.05, float((float(x2) - float(x1)) / 443.0)),str(comment['style']),str(comment['circle'])))  # Use converted values

    if (qaree_key == "A"): #if warsh add common things to asbahani and kalon todo abujafar after subject matter experts verify
        c.execute("""
            INSERT INTO shmrly(qaree, page_number, color, type, x, y, width, style, circle)
            SELECT ?, page_number, color, type, x, y, width, style, circle
            FROM shmrly
            WHERE (qaree = ?) AND ((color IN (?, ?)) or (circle = ?))
        """, ("W", "A", "olive", "blue", "4"))
        c.execute("""
            INSERT INTO shmrly(qaree, page_number, color, type, x, y, width, style, circle)
            SELECT ?, page_number, color, type, x, y, width, style, circle
            FROM shmrly
            WHERE qaree = ? AND circle = ?
        """, ("K", "A", "4"))
        c.execute("UPDATE shmrly SET X=x+0.02 where circle='4' and qaree=?",(qaree_key))
    if qaree_key in ["C", "D", "G"]:
        c.execute("UPDATE shmrly SET X = X + CASE WHEN (page_number % 2) = 0 THEN 0.13 ELSE -0.10 END WHERE qaree = ?", (qaree_key,))
    #twice for safety
    c.execute("UPDATE shmrly SET circle='' where circle is null")

    #if ibnamer add hesham and ibn thakwan as separate qaree
    if (qaree_key == "I"): #if  ibn amer then create hesahm and ibn thakwan hesham = circle =1 or '' and ibnthkwan circle =2 or ''
        c.execute("""
            INSERT INTO shmrly(qaree, page_number, color, type, x, y, width, style, circle)
            SELECT ?, page_number, color, type, x, y, width, style, circle
            FROM shmrly
            WHERE (qaree = ?) AND  (circle in('','1','4'))
        """, ("H", "I"))
        c.execute("""
            INSERT INTO shmrly(qaree, page_number, color, type, x, y, width, style, circle)
            SELECT ?, page_number, color, type, x, y, width, style, circle
            FROM shmrly
            WHERE (qaree = ?) AND  (circle in('','2','4'))
        """, ("Z", "I"))
    
    
    c.execute("UPDATE shmrly SET style='S' where style is null")
    c.execute("UPDATE shmrly SET circle='' where circle is null")

    conn.commit()
    conn.close()

import webcolors

def apply_fixed_mappings(rgb_values_original):
    fixed_mappings = {
        (255, 173, 90): (255, 153, 51),
        (190, 190, 0): (204, 204, 0),
        (179, 179, 0): (204, 204, 51),
        (229, 34, 55): (204, 0, 51),
        (204, 204, 0): (255, 255, 0),
        (255, 104, 32): (255, 140, 0),
        (50, 255, 50): (50, 205, 50),
        (158, 106, 25): (139, 69, 19),   # Mapping for (158, 106, 25) to Saddle Brown
        (0, 123, 255): (30, 144, 255),   # Mapping for (0, 123, 255) to Dodger Blue
        (204, 0, 51): (220, 20, 60),     # Custom mapping for (204, 0, 51) to Crimson
        (204, 204, 51): (218, 165, 32),  # Custom mapping for (204, 204, 51) to Goldenrod
        (128, 0, 255): (128, 0, 128),    # Mapping for (128, 0, 255) to Purple
        (0, 136, 0): (0, 128, 0),        # Mapping for (0, 136, 0) to Green
        (0, 127, 255): (0, 0, 255),      # Mapping for (0, 127, 255) to Blue
        (128, 128, 192): (128, 128, 128), # Mapping for (128, 128, 192) to Gray
        (139, 69, 16): (139, 69, 19),     # Mapping for (139, 69, 16) to Saddle Brown
    }
    if rgb_values_original in fixed_mappings:
        return fixed_mappings[rgb_values_original]
    
    return rgb_values_original

def get_nearest_web_color(color):
    try:
        # Attempt to parse the input color (can be a name, RGB tuple, or hex code)
        rgb_values = webcolors.name_to_rgb(color) if isinstance(color, str) else webcolors.hex_to_rgb(color)
    except ValueError:
        raise ValueError("Invalid color input. Provide a valid color name, RGB tuple, or hex code.")

    min_distance = float('inf')
    nearest_color_name = None

    for color_name, color_hex in webcolors.CSS3_HEX_TO_NAMES.items():
        color_rgb = webcolors.hex_to_rgb(color_hex)
        distance = sum((val1 - val2) ** 2 for val1, val2 in zip(rgb_values, color_rgb))
        if distance < min_distance:
            min_distance = distance
            nearest_color_name = color_name

    return nearest_color_name

def get_color_name(color_values,qaree_key):
    try:
        fraction_values = eval(color_values)
        rgb_values_original = tuple(int(round(val * 255)) for val in fraction_values)
        
        # Apply fixed mappings first
        rgb_values_mapped = apply_fixed_mappings(rgb_values_original)
        try:
            color_name = webcolors.rgb_to_name(rgb_values_mapped)
        except ValueError:
            color_name = get_nearest_web_color(rgb_values_mapped)
    except Exception:
        failed_colors.add(qaree_key+ ' '+str(rgb_values_mapped)+str(rgb_values_original))  # Add the failed color to the set
        color_name = 'red'
    
    return color_name




def get_color_type(color_values):
    return ""
    # if color_values == "red":
    #     return "Farsh"
    # elif (color_values == "green") or (color_values == "lime") :
    #     return "Ebdal"
    # elif color_values == "cyan":
    #     return "Sound"
    # elif color_values == "blue":
    #     return "Naql"
    # elif (color_values == "magenta") or (color_values == "purple"):
    #     return "Badal+Leen"
    # elif (color_values == "yellow") or (color_values == "olive"):
    #     return "MeemSela"

    
    # else:
    #     return "Farsh"


def process_qaree_key(qaree_key):
    qaree_files = {
        "W": 'e:/Qeraat/Warsh-Asbahani-Shamarly-Shalaby.pdf',
        "I": 'e:/Qeraat/IbnAmer-Shamarly-Shalaby.pdf',
        "T": 'e:/Qeraat/madina10th.pdf',
        "J": 'e:/Qeraat/AbuJaafar-Shamarly-Shalaby.pdf',
        "K": 'e:/Qeraat/Qaloon-Shamarly-Shalaby.pdf',
        "U": 'e:/Qeraat/AshabSela-Shamrly-Shalaby.pdf',
        "M": 'e:/Qeraat/Hamzah-Shamarly-Shalaby.pdf',
        "B": 'e:/Qeraat/IbnKatheer-Shmarly-Shalaby.pdf',
        "S": 'e:/Qeraat/Sho3ba-Shamarly-Shalaby.pdf',
        "A": 'e:/Qeraat/Warsh-Azraq-Shamarly-Shalaby_V1_1.pdf',
        "E": 'e:/Qeraat/Kisai-Shamarly-Shalaby.pdf',
        "F": 'e:/Qeraat/Khalaf-Shamarly-Shalaby.pdf',
        "X": 'e:/Qeraat/Kisai-Khalaf-Shamarly-Shalaby.pdf',
        "Y": 'e:/Qeraat/Yaaqoub-Shamarly-Shalaby.pdf',
        "C": 'e:/Qeraat/AbuAmro-Shamarly-Shalaby.pdf',
        "D": 'e:/Qeraat/Dori-AbuAmro-Shamarly-Shalaby.pdf',
        "G": 'e:/Qeraat/Sosi-AbuAmro-Shamarly-Shalaby.pdf',
        "L": 'e:/Qeraat/Tawasot-Shamarly-Shalaby.pdf',
        "O": 'e:/Qeraat/Asem_IbnAmer-Shamarly-Shalaby.pdf',
        "P": 'e:/Qeraat/AbuAmro-Yaqoub-Shamarly-Shalaby.pdf',
         
    }

    if qaree_key == "ALL":
        for key, pdf_path in qaree_files.items():
            if os.path.exists(pdf_path):
                comments = extract_line_comments(pdf_path)
                insert_comments_sqlite(comments, key)
                print("Line comments extracted and inserted from", pdf_path)
            else:
                print("File not found:", pdf_path)
    elif qaree_key in qaree_files:
        pdf_path = qaree_files[qaree_key]
        if os.path.exists(pdf_path):
            comments = extract_line_comments(pdf_path)
            insert_comments_sqlite(comments, qaree_key)
            print("Line comments extracted and inserted from", pdf_path)
        else:
            print("File not found:", pdf_path)
    else:
        print("Invalid qaree key entered!")

# Extract line comments from the PDF
failed_colors = set()
qaree_key = input("Enter the qaree key (A for Warsh, W for Asbahani, I for IbnAmer, T for Tayseer, J for AbuJaafar, K for Qaloon, U for AshabSela, M for Hamzah, B for IbnKatheer, S for Sho3ba, or ALL for all files): ").upper()
process_qaree_key(qaree_key)

file_path = 'E:/Qeraat/farsh_v6.db'
destination_folders = [
    'E:/Qeraat/Wursha_QuranHolder/other/data/',
    'E:/Qeraat/Wursha_QuranHolder/platforms/android/app/build/intermediates/assets/debug/mergeDebugAssets/www/',
    'E:/Qeraat/Wursha_QuranHolder/platforms/android/app/src/main/assets/www/',
    'E:/Qeraat/Wursha_QuranHolder/www/',
]


for folder in destination_folders:
    destination_file = folder + 'farsh_v6.db'
    try:
        shutil.copy(file_path, destination_file)
        print(f"File copied to {destination_file} successfully.")
    except FileNotFoundError:
        print(f"Error: The source file {file_path} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when copying to {destination_file}.")
    except Exception as e:
        print(f"An error occurred while copying to {destination_file}: {str(e)}")


# #add to archive
# zip_file_path = "E:/Qeraat/Wursha_QuranHolder/other/data/farsh_v6.db.zip"
# with zipfile.ZipFile(zip_file_path, 'r+') as zip_file:
#     zip_file.write(file_path, arcname='farsh_v4.db')
print("Distinct Failed Colors:", failed_colors)
print("File copied to the specified folders.")
