import sqlite3
import fitz  # PyMuPDF

def add_lines_as_comments(input_pdf, output_pdf, db_file, line_width=1):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT page_number, color, x, y, width FROM madina_temp")
    data = cursor.fetchall()
    conn.close()

    doc = fitz.open(input_pdf)

    for row in data:
        page_number = row[0]
        page = doc[page_number - 1]  # Adjust page index as PyMuPDF starts from 0
        page_width = page.mediabox.width
        page_height = page.mediabox.height

        page_width1 = 254
        page_height1 = 412
        xmargin = 88 if page_number % 2 == 0 else 40
        ymargin = 65

        if row[2] is None or row[3] is None or row[4] is None:
            continue  # Skip if any necessary value is None

        # Assuming row[2], row[3], row[4] are in percentage
        x = float(row[2]) * page_width1 + xmargin
        y = (1 - float(row[3])) * page_height1 + ymargin
        width = float(row[4]) * page_width1

        # Convert to PDF units (points)
        x_start = max(0, min(x, page_width))
        y_start = max(0, min(y, page_height))
        x_end = max(0, min(x + width, page_width))
        y_end = y_start

        # Convert hex color to RGB
        color = tuple(int(row[1][i:i+2], 16) / 255 for i in (1, 3, 5))

        # Create a line annotation
        print(f"Coordinates: x_start={x_start}, y_start={y_start}, x_end={x_end}, y_end={y_end}")
        annot = page.add_line_annot(fitz.Rect(x_start, y_start, x_end, y_end + line_width), [x_start, y_start, x_end, y_end])
        annot.set_colors(stroke=color)
        annot.set_border(width=line_width)
        annot.update()
        annot.set_info({
            "L": [x_start, y_start, x_end, y_end],
            "BS": {"W": line_width},
            "C": color,
        })
        annot.update()

    doc.save(output_pdf)

# Example usage
add_lines_as_comments("E:/Qeraat/Madina.pdf", "E:/Qeraat/Madina_wlines_comments.pdf", "E:/Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db", line_width=3)
