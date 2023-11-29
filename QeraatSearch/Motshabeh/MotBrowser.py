import sqlite3
from tkinter import Tk, Label, Listbox, Button, Scrollbar, messagebox

class SimilarityTunerApp:
    def __init__(self, master):
        self.master = master
        master.title("Similarity Tuner")

        # Connect to the SQLite database
        self.connection = sqlite3.connect(r'E:/Qeraat/QeraatFasrhTools/QeraatSearch/Motshabeh/motshabeh.db')
        self.cursor = self.connection.cursor()

        # Initialize GUI components
        self.label = Label(master, text="Similarity Tuner")
        self.label.pack()

        self.listbox = Listbox(master, selectmode="multiple", yscrollcommand=True, width=100, height=20)
        self.listbox.pack()

        self.scrollbar = Scrollbar(master, command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.add_button = Button(master, text="Add Selected Rows", command=self.add_selected_rows)
        self.add_button.pack()

        self.search_button = Button(master, text="Search Ayas", command=self.search_ayas)
        self.search_button.pack()

        self.refresh_listbox()

    def refresh_listbox(self):
        self.listbox.delete(0, "end")

        # Fetch data from the similarity_matrix table
        self.cursor.execute("SELECT * FROM MotshabehatU")
        rows = self.cursor.fetchall()

        # Display data in the listbox
        for row in rows:
            self.listbox.insert("end", f"{row[0]} - {row[1]} - {row[8]:.2f}%")

    def add_selected_rows(self):
        selected_indices = [int(i.split()[0]) for i in self.listbox.curselection()]

        if selected_indices:
            # Mark selected rows as not important or perform any desired action
            messagebox.showinfo("Action", f"Marked rows {', '.join(map(str, selected_indices))} as not important.")

            # You can implement further logic here to update the database or perform other actions

            # Refresh the listbox after the action
            self.refresh_listbox()
        else:
            messagebox.showinfo("Info", "No rows selected.")

    def search_ayas(self):
        # Implement the logic to search for ayas and add them to the similarity table
        # This is a placeholder for your specific search and add logic
        # You can use additional GUI elements and functionality to perform the search and selection

        # Example: Fetch ayas from the book_quran table
        self.cursor.execute("SELECT aya_index, text FROM book_quran LIMIT 10")
        ayas = self.cursor.fetchall()

        # Display fetched ayas in a separate window or using additional GUI elements
        search_window = Tk()
        search_window.title("Search Ayas")

        search_listbox = Listbox(search_window, selectmode="multiple", yscrollcommand=True, width=100, height=20)
        search_listbox.pack()

        for aya_index, aya_text in ayas:
            search_listbox.insert("end", f"{aya_index} - {aya_text}")

        add_selected_button = Button(search_window, text="Add Selected Ayas", command=lambda: self.add_selected_ayas(search_listbox))
        add_selected_button.pack()

    def add_selected_ayas(self, search_listbox):
        selected_ayas_indices = [int(i.split()[0]) for i in search_listbox.curselection()]

        if selected_ayas_indices:
            # Implement the logic to add selected ayas to the similarity table
            # This is a placeholder for your specific add logic
            # You can use additional GUI elements and functionality to perform the add operation

            # Example: Display a message
            messagebox.showinfo("Action", f"Added selected ayas {', '.join(map(str, selected_ayas_indices))} to the similarity table.")

            # Refresh the listbox after the action
            self.refresh_listbox()
        else:
            messagebox.showinfo("Info", "No ayas selected for addition.")

if __name__ == "__main__":
    root = Tk()
    app = SimilarityTunerApp(root)
    root.mainloop()
