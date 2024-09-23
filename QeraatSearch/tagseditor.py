import sqlite3
from tkinter import *
from tkinter import ttk

def fetch_aggregated_data():
    query = """
    SELECT reading, count(*), group_concat(DISTINCT sub_subject), group_concat(DISTINCT qarees)
    FROM quran_data
    WHERE done IS NULL AND r5_2 IS NULL
    GROUP BY reading
    ORDER BY count(*) DESC
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        tree1.insert("", "end", values=row)

def on_first_grid_select(event):
    # Clear the second grid first
    for item in tree2.get_children():
        tree2.delete(item)
        
    selected_item = tree1.selection()[0]
    selected_reading = tree1.item(selected_item)['values'][0]
    fetch_detailed_data(selected_reading)

def fetch_detailed_data(reading):
    query = """
    SELECT aya_index, id, sora, aya, sub_subject, qarees, reading, tags, page_number1, page_number2, readingresult, qareesrest, count_words, sub_sno, resultnew, wordsno, done 
    FROM quran_data
    WHERE reading = ?
    """
    cursor.execute(query, (reading,))
    rows = cursor.fetchall()
    for row in rows:
        tree2.insert("", "end", values=row)

def on_double_click(event):
    # Handle double click on the second grid to edit cell
    selected_item = tree2.selection()[0]
    col = tree2.identify_column(event.x)
    col_index = int(col.replace("#", "")) - 1  # Treeview columns are 1-based
    edit_cell(tree2, selected_item, col_index)

def edit_cell(treeview, item, col_index):
    # Create a popup for editing the cell
    col_values = treeview.item(item, 'values')
    value_to_edit = col_values[col_index]

    # Popup window
    edit_popup = Toplevel(root)
    edit_popup.title("Edit Cell")

    Label(edit_popup, text="New Value:").pack()
    new_value = Entry(edit_popup)
    new_value.insert(0, value_to_edit)
    new_value.pack()

    def save_edit():
        updated_values = list(col_values)
        updated_values[col_index] = new_value.get()
        treeview.item(item, values=updated_values)
        edit_popup.destroy()

    Button(edit_popup, text="Save", command=save_edit).pack()

def update_record():
    # Get selected item from second grid, make changes, and commit to DB
    selected_item = tree2.selection()[0]
    updated_values = tree2.item(selected_item)['values']
    query = """
    UPDATE quran_data
    SET qareesrest = ?, resultnew = ?, Done = ?
    WHERE id = ?
    """
    cursor.execute(query, (updated_values[11], updated_values[14], updated_values[16], updated_values[1]))
    conn.commit()

# Connect to SQLite DB
conn = sqlite3.connect("E:/Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db")
cursor = conn.cursor()

# Create the UI window
root = Tk()
root.title("Quran Data Query")
root.geometry("1000x600")

# Set grid layout to expand properly
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# First grid - Aggregate data
tree1_frame = Frame(root)
tree1_frame.grid(row=0, column=0, sticky='nsew')

tree1 = ttk.Treeview(tree1_frame, columns=("reading", "count", "sub_subjects", "qarees"), show="headings")
tree1.heading("reading", text="Reading")
tree1.heading("count", text="Count")
tree1.heading("sub_subjects", text="Sub Subjects")
tree1.heading("qarees", text="Qarees")
tree1.pack(fill=BOTH, expand=True)

# Bind the selection event to load details in the second grid
tree1.bind("<<TreeviewSelect>>", on_first_grid_select)

# Second grid - Detailed rows
tree2_frame = Frame(root)
tree2_frame.grid(row=1, column=0, sticky='nsew')

tree2 = ttk.Treeview(tree2_frame, columns=("aya_index", "id", "sora", "aya", "sub_subject", "qarees", "reading", "tags", "page_number1", "page_number2", "readingresult", "qareesrest", "count_words", "sub_sno", "resultnew", "wordsno", "done"), show="headings")
tree2.heading("aya_index", text="Aya Index")
tree2.heading("id", text="ID")
tree2.heading("sora", text="Sora")
tree2.heading("aya", text="Aya")
tree2.heading("sub_subject", text="Sub Subject")
tree2.heading("qarees", text="Qarees")
tree2.heading("reading", text="Reading")
tree2.heading("tags", text="Tags")
tree2.heading("page_number1", text="Page Number 1")
tree2.heading("page_number2", text="Page Number 2")
tree2.heading("readingresult", text="Reading Result")
tree2.heading("qareesrest", text="Qarees Rest")
tree2.heading("count_words", text="Count Words")
tree2.heading("sub_sno", text="Sub S No")
tree2.heading("resultnew", text="Result New")
tree2.heading("wordsno", text="Words No")
tree2.heading("done", text="Done")
tree2.pack(fill=BOTH, expand=True)

# Bind double-click to edit cells in second grid
tree2.bind("<Double-1>", on_double_click)

# Update button for committing changes
update_btn = Button(root, text="Update Record", command=update_record)
update_btn.grid(row=2, column=0, pady=20)

# Fetch the aggregate data on load
fetch_aggregated_data()

# Start the Tkinter loop
root.mainloop()
