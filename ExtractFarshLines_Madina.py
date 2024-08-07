import os
import shutil
import sqlite3
import re
from PyPDF2 import PdfReader
import webcolors
script_path = os.path.abspath(__file__)
drive, _ = os.path.splitdrive(script_path) 
drive = drive +'/'
db_path = os.path.join(drive, 'Qeraat', 'farsh_v7.db')
tmp_db_path = os.path.join(drive, 'Qeraat', 'tmp.db')
qaree_files = {
    "W": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'Warsh-Asbahani-Madina-Shalaby.pdf'),
    "I": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'IbnAmer-Madina-Shalaby.pdf'),
    "T": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'Madina10th.pdf'),
    "J": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'AbuJaafar-Madina-Shalaby.pdf'),
    "K": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'Qaloon-Madina-Shalaby.pdf'),
    "U": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'AshabSela-Shamrly-Shalaby.pdf'),
    "M": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'Hamzah-Madina-Shalaby.pdf'),
    "B": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'IbnKatheer-Madina-Shalaby.pdf'),
    "S": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'Sho3ba-Madina-Shalaby.pdf'),
    "A": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'Warsh-Madina-Shalaby.pdf'),
    "R": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'Warsh-Madina-Shalaby_Light.pdf'),
    "E": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'Kisai-Madina-Shalaby.pdf'),
    "F": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'Khalaf-Madina-Shalaby.pdf'),
    "X": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'Kisai-Khalaf-Madina-Shalaby.pdf'),
    "Y": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'Yaaqoub-Madina-Shalaby.pdf'),
    "C": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'AbuAmro-Madina-Shalaby.pdf'),
    # "D": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'Dori-AbuAmro-Madina-Shalaby.pdf'),
    # "G": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'Sosi-AbuAmro-Madina-Shalaby.pdf'),
    "L": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'Tawasot-Madina-Shalaby.pdf'),
    "O": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'Asem_IbnAmer-Madina-Shalaby.pdf'),
    "P": os.path.join(drive, 'Qeraat', 'QeraatFasrhTools_Data', 'MusshafM', 'AbuAmro-Yaqoub-Madina-Shalaby.pdf'),
}

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
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS madina
                 (qaree TEXT, page_number INTEGER, color TEXT, x REAL, y REAL, width REAL)''')
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
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # Delete rows with value "A" in the field "qaree"
    c.execute("DELETE FROM madina WHERE qaree = ?", (qaree_key,))
    if qaree_key == "I":
        c.execute("DELETE FROM madina WHERE qaree = 'H'") # Hesham is subset of ibnamer
        c.execute("DELETE FROM madina WHERE qaree = 'Z'") # Ibn thakwan is a subset of ibnamer
    if qaree_key == "C":
        c.execute("DELETE FROM madina WHERE qaree = 'D'") # Dori is subset of AbuAmro
        c.execute("DELETE FROM madina WHERE qaree = 'G'") # Sosi is a subset of AbuAmro


    
    for comment in comments:
        # print(comment['content'], comment['coordinates'], comment['color'])
        yshift = 65.0
        if comment['pageno']<3:
            yshift = 95.0
            if comment['pageno'] % 2 == 0:
                xshift = 110.0
            else:
                xshift= 10
        elif comment['pageno'] % 2 == 0:
            xshift = 86.0
        else:
            xshift= 42.0

        coordinates = str(comment['coordinates'])
        matches = re.findall(r'(\d+\.?\d*)', coordinates)
        x1, y1, x2, y2 = matches

        color_values = get_color_name(str(comment['color']),qaree_key)
        if qaree_key != 'T':
            color_type = get_color_type(color_values)
        else:
            color_type = 'Tayseer'
        c.execute("INSERT INTO madina(qaree, page_number, color, x, y, width,style,circle) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (qaree_key, comment['pageno'], str(color_values), float((float(x1)-xshift)/255.0), 1-(float((float(y1)-yshift)/410.0)),max(0.05, float((float(x2) - float(x1)) / 255.0)),str(comment['style']),str(comment['circle'])))  # Use converted values
    if (qaree_key == "M"):
        c.execute("update madina set circle =4 where qaree='M' and color='cyan' and circle='2' and width<=0.05")
        c.execute("UPDATE madina SET X=x+0.02 where circle='4' and qaree=?",(qaree_key))
    #shift circle object left
    if (qaree_key in ["B","X","A","W","K"]):
        c.execute("UPDATE madina SET X=x+0.02 where circle='4' and qaree=?",(qaree_key))
    #twice for safety
    c.execute("UPDATE madina SET circle='' where circle is null")

    #if ibnamer add hesham and ibn thakwan as separate qaree
    if (qaree_key == "I"): #if  ibn amer then create hesahm and ibn thakwan hesham = circle =1 or '' and ibnthkwan circle =2 or ''
        c.execute("""
            INSERT INTO madina(qaree, page_number, color, x, y, width, style, circle)
            SELECT ?, page_number, color, x, y, width, style, circle
            FROM madina
            WHERE (qaree = ?) AND  (circle in('','1','4'))
        """, ("H", "I"))
        c.execute("""
            INSERT INTO madina(qaree, page_number, color, x, y, width, style, circle)
            SELECT ?, page_number, color, x, y, width, style, circle
            FROM madina
            WHERE (qaree = ?) AND  (circle in('','2','4'))
        """, ("Z", "I"))
    #if AbuAmro add Dori and Sosi as separate qaree
    if (qaree_key == "C"): #if  ibn amer then create hesahm and ibn thakwan hesham = circle =1 or '' and ibnthkwan circle =2 or ''
        c.execute("""
            INSERT INTO madina(qaree, page_number, color, x, y, width, style, circle)
            SELECT ?, page_number, color, x, y, width, style, circle
            FROM madina
            WHERE (qaree = ?) AND  (circle in('','1','4'))
        """, ("D", "C"))
        c.execute("""
            INSERT INTO madina(qaree, page_number, color, x, y, width, style, circle)
            SELECT ?, page_number, color, x, y, width, style, circle
            FROM madina
            WHERE (qaree = ?) AND  (circle in('','2','4'))
        """, ("G", "C"))
    
    
    c.execute("UPDATE madina SET style='S' where style is null")
    c.execute("UPDATE madina SET circle='' where circle is null")

    conn.commit()
    conn.close()

import webcolors


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
        

        # try:
        #     color_name = webcolors.rgb_to_name(rgb_values_original)
        # except ValueError:
        color_name = '#{:02x}{:02x}{:02x}'.format(*rgb_values_original)
    except Exception:
        failed_colors.add(qaree_key+ ' '+str(rgb_values_original))  # Add the failed color to the set
        color_name = 'red'
    
    return color_name


def get_color_type(color_values):
    return ""


def process_qaree_key(qaree_key):
    file_path = db_path
    tmp_file = tmp_db_path
    shutil.copy2(file_path, tmp_file)

    def is_newer(file1, file2):
        return os.path.getmtime(file1) > os.path.getmtime(file2)

    if qaree_key == "ALL":
        for key, pdf_path in qaree_files.items():
            if os.path.exists(pdf_path):
                comments = extract_line_comments(pdf_path)
                insert_comments_sqlite(comments, key)
                print("Line comments extracted and inserted from", pdf_path)
            else:
                print("File not found:", pdf_path)
    elif qaree_key == "NEW":
        for key, pdf_path in qaree_files.items():
            if os.path.exists(pdf_path):
                if  is_newer(pdf_path, tmp_file):
                    comments = extract_line_comments(pdf_path)
                    insert_comments_sqlite(comments, key)
                    print("Line comments extracted and inserted from", pdf_path)
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
qaree_key = input("Enter the qaree key (New for Updated Only or ALL for all files): ").upper()
if qaree_key == "":
    qaree_key= "NEW"
process_qaree_key(qaree_key)

file_path = db_path
destination_folders = [
    os.path.join(drive, 'Qeraat', 'Wursha_QuranHolder', 'other', 'data'),
    os.path.join(drive, 'Qeraat', 'Wursha_QuranHolder', 'platforms', 'android', 'app', 'build', 'intermediates', 'assets', 'debug', 'mergeDebugAssets', 'www'),
    os.path.join(drive, 'Qeraat', 'Wursha_QuranHolder', 'platforms', 'android', 'app', 'src', 'main', 'assets', 'www'),
    os.path.join(drive, 'Qeraat', 'Wursha_QuranHolder', 'www'),
    os.path.join(drive, 'Qeraat', 'quran-api'),
]


for folder in destination_folders:
    destination_file = folder + '/farsh_v7.db'
    try:
        shutil.copy(file_path, destination_file)
        print(f"File copied to {destination_file} successfully.")
    except FileNotFoundError:
        print(f"Error: The source file {file_path} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when copying to {destination_file}.")
    except Exception as e:
        print(f"An error occurred while copying to {destination_file}: {str(e)}")


print("File copied to the specified folders.")
