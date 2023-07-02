import tkinter as tk
import sqlite3
from PIL import Image, ImageTk, ImageDraw

class QuranBrowserApp:
    def __init__(self, root):
        self.root = root
        self.current_page = 2
        self.quran_pages = []  # List to store Quran page image paths
        self.db_connection = None
        self.page_image = None
        # Load Quran page images
        self.load_quran_pages()

        # Connect to the SQLite database
        self.connect_to_database()

        # Create GUI components
        self.create_gui()

    def load_quran_pages(self):
        # Assuming Quran page images are named as "page1.jpg", "page2.jpg", etc.
        for i in range(2, 522):
            page_image_path = f"E:/Qeraat/QeraatFasrhTools/QuranWordMap/pages/{i}.png"
            self.quran_pages.append(page_image_path)

    def connect_to_database(self):
        # Connect to the SQLite database
        self.db_connection = sqlite3.connect("E:/Qeraat/QeraatFasrhTools/QuranWordMap/quran.db")
        self.db_connection.row_factory = sqlite3.Row  # Enable accessing rows as dictionaries

    def create_gui(self):
        # Main window
        self.root.title("Quran Browser")
        self.root.geometry("900x600")
        self.root.resizable(True, True)

        # Quran page image display area
        self.page_canvas = tk.Canvas(self.root, width=600, height=600)
        self.page_canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Create a scroll bar for the listbox
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Side grid for Quran words
        self.words_listbox = tk.Listbox(self.root, width=40, justify=tk.RIGHT, font=("Arial", 14), yscrollcommand=scrollbar.set)  # Right aligned, larger font, with scroll bar
        self.words_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Configure the scroll bar to control the listbox
        scrollbar.config(command=self.words_listbox.yview)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_page)
        self.next_button.place(x=500, y=560)

        # Previous page button
        self.prev_button = tk.Button(self.root, text="Previous", command=self.prev_page)
        self.prev_button.place(x=420, y=560)

        # Bind mouse click event to the Quran page image display area
        self.page_canvas.bind("<Button-1>", self.on_page_click)

        # Bind the shortcut key
        self.bind_shortcut_key()

        # Display the initial page and words
        self.display_page(self.current_page)
        self.display_words(self.current_page)

    def display_page(self, page_number):
        # Load and display the page image using Pillow
        page_image_path = self.quran_pages[self.current_page - 2]
        self.page_image = Image.open(page_image_path)
        self.page_image.thumbnail((600, 600))  # Preserve aspect ratio while resizing
        page_image_tk = ImageTk.PhotoImage(self.page_image)
        self.page_canvas.create_image(0, 0, anchor=tk.NW, image=page_image_tk)
        self.page_canvas.image = page_image_tk  # Store a reference to avoid garbage collection
        page_label = tk.Label(self.root, text=f"Page: {page_number}")
        page_label.place(x=500, y=460)

    def display_words(self, page_number):
        # Clear the previous words in the listbox
        self.words_listbox.delete(0, tk.END)

        # Fetch word data for the current page from the database
        query = "SELECT word, startx, starty, ayah FROM words WHERE pageno = ?"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (page_number,))
        word_data = cursor.fetchall()
        # Display the words in the listbox and draw red lines for words with coordinates
        for row in word_data:
            word = row[0]  # Access the first element in the tuple
            start_x = row[1]
            start_y = row[2]
            ayah = row[3]
            self.words_listbox.insert(tk.END, f"{ayah} : {word} ")
            if start_x is not None and start_y is not None:
                # Draw a red line for the word with coordinates
                self.draw_red_line(start_x, start_y)

    def draw_red_line(self, start_x, start_y):
        # Create an ImageDraw object to draw on the original page image
        draw = ImageDraw.Draw(self.page_image)

        # Define the line parameters
        line_color = (255, 0, 0)  # Red color (R, G, B)
        line_thickness = 3
        line_length = 30

        # Calculate the line start and end coordinates
        end_x = start_x + line_length
        end_y = start_y

        # Draw the line
        draw.line([(start_x, start_y), (end_x, end_y)], fill=line_color, width=line_thickness)

        # Update the image in the canvas
        page_image_tk = ImageTk.PhotoImage(self.page_image)
        self.page_canvas.create_image(0, 0, anchor=tk.NW, image=page_image_tk)
        self.page_canvas.image = page_image_tk  # Store a reference to avoid garbage collection

    def next_page(self):
        if self.current_page < len(self.quran_pages):
            self.current_page += 1
            self.display_page(self.current_page)
            self.display_words(self.current_page)

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.display_page(self.current_page)
            self.display_words(self.current_page)

    def on_page_click(self, event):
        # Get the clicked coordinates
        x = event.x
        y = event.y

        # Get the selected index of the clicked word in the listbox
        selected_index = self.words_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
        else:
            return

        # Get the word data for the clicked index from the list
        word_data = self.get_word_data_for_page(self.current_page)
        if selected_index < len(word_data):
            clicked_row = word_data[selected_index]
            clicked_word = clicked_row["word"]
            clicked_word_index = clicked_row["wordindex"]
            pageno = clicked_row["pageno"]

            # Update the coordinates in the database for the clicked word
            self.update_word_coordinates(clicked_word_index, x, y)
            # self.change_contour_color(x, y)
            self.draw_red_line(x, y)
            print(f"Clicked word: {clicked_word} at coordinates ({x}, {y})")

    def update_word_coordinates(self, wordindex, x, y):
        # Update the startx and starty coordinates in the database for the given word
        query = "UPDATE words SET startx = ?, starty = ? WHERE wordindex = ?"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (x, y, wordindex))
        self.db_connection.commit()

    def get_word_data_for_page(self, page_number):
        # Fetch word data for the current page from the database
        query = "SELECT * FROM words WHERE pageno = ?"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (page_number,))
        word_data = cursor.fetchall()
        return word_data

    def bind_shortcut_key(self):
        # Bind the "n" key to go to the next word
        self.root.bind("n", lambda event: self.next_page())

    def run(self):
        self.root.mainloop()


# Create and run the app
root = tk.Tk()
app = QuranBrowserApp(root)
app.run()
