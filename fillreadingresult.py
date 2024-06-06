import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class QuranApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quran Result Editor")
        self.root.geometry("800x400")
        self.create_widgets()

        # Connect to the SQLite database
        self.conn = sqlite3.connect('D:/Qeraat/QeraatFasrhTools/QeraatSearch/qeraat_data_simple.db')  # Change this to your database file
        self.cursor = self.conn.cursor()

        # Load SQL query from file
        with open('D:/Qeraat/QeraatFasrhTools/QeraatSearch/Farsh_Words.sql', 'r', encoding='utf-8') as file:
            self.query = file.read()

        # Fetch initial data
        self.cursor.execute(self.query)
        self.records = self.cursor.fetchall()
        self.current_index = 0
        self.display_record()

    def create_widgets(self):
        # Create form fields
        self.text_full = tk.StringVar()
        self.aya_index = tk.StringVar()
        self.id = tk.StringVar()
        self.sub_subject = tk.StringVar()
        self.reading = tk.StringVar()
        self.qareesrest = tk.StringVar()
        self.resultnew = tk.StringVar()

        self.create_form_field("نص الآية", self.text_full)
        self.create_form_field("ترتيب الآية", self.aya_index)
        self.create_form_field("#", self.id)
        self.create_form_field("الكلمة", self.sub_subject)
        self.create_form_field("القراءة", self.reading)
        self.create_form_field("القراء", self.qareesrest)
        self.create_form_field("النتيجة", self.resultnew, focus=True)

        # Create buttons area
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill=tk.X, padx=10, pady=10)

        # Add action buttons to button frame
        self.update_similar_button = ttk.Button(button_frame, text="Update Similar", command=self.update_similar)
        self.update_similar_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.copy_button = ttk.Button(button_frame, text="نسخ المصدر", command=self.copy_sub_subject)
        self.copy_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.append_wosla_button = ttk.Button(button_frame, text=" 'وصلا'", command=lambda: self.append_to_resultnew(" وصلا"))
        self.append_wosla_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.append_waqfa_button = ttk.Button(button_frame, text=" 'وقفا'", command=lambda: self.append_to_resultnew(" وقفا"))
        self.append_waqfa_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.append_wosla_waqfa_button = ttk.Button(button_frame, text=" 'وصلا ووقفا'", command=lambda: self.append_to_resultnew(" وصلا ووقفا"))
        self.append_wosla_waqfa_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.prev_button = ttk.Button(button_frame, text="سابق", command=self.prev_record)
        self.prev_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.next_button = ttk.Button(button_frame, text="تالي", command=self.next_record)
        self.next_button.pack(side=tk.LEFT, padx=5, pady=5)

    def create_form_field(self, label_text, variable, focus=False):
        frame = ttk.Frame(self.root)
        frame.pack(fill=tk.X, padx=10, pady=5)
        label = ttk.Label(frame, text=label_text)
        label.pack(side=tk.RIGHT)
        entry = ttk.Entry(frame, textvariable=variable, width=50, justify='right')
        entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        if focus:
            entry.focus_set()

    def display_record(self):
        if self.records:
            record = self.records[self.current_index]
            self.text_full.set(record[0])
            self.aya_index.set(record[1])
            self.id.set(record[2])
            self.sub_subject.set(record[3])
            self.reading.set(record[4])
            self.qareesrest.set(record[5])
            self.resultnew.set(record[6])

    def prev_record(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.display_record()

    def next_record(self):
        if self.current_index < len(self.records) - 1:
            self.current_index += 1
            self.display_record()

    def copy_sub_subject(self):
        self.resultnew.set(self.sub_subject.get())

    def append_to_resultnew(self, text):
        self.resultnew.set(self.resultnew.get() + text)

    def update_similar(self):
        try:
            update_query = '''
                UPDATE quran_data
                SET resultnew = a.resultnew
                FROM quran_data AS a
                WHERE quran_data.resultnew IS NULL
                AND a.resultnew IS NOT NULL
                AND a.sub_subject = quran_data.sub_subject
                AND a.reading = quran_data.reading;
            '''
            self.cursor.execute(update_query)
            self.conn.commit()
            messagebox.showinfo("Update Successful", "All similar records have been updated.")
        except sqlite3.Error as e:
            messagebox.showerror("Update Failed", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuranApp(root)
    root.mainloop()
