import sqlite3
import tkinter as tk
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
        """Load Quran page image paths."""
        for i in range(2, 522):
            page_image_path = f"E:/Qeraat/QeraatFasrhTools_Data/pages/{i}.png"
            self.quran_pages.append(page_image_path)

    def connect_to_database(self):
        """Connect to the SQLite database."""
        try:
            self.db_connection = sqlite3.connect("E:/Qeraat/QeraatFasrhTools/QuranWordMap/quran.db")
            self.db_connection.row_factory = sqlite3.Row  # Enable accessing rows as dictionaries
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def create_gui(self):
        """Create the GUI layout."""
        self.root.title("Quran Browser")
        self.root.geometry("900x600")
        self.root.resizable(True, True)

        # Quran page display area
        self.page_canvas = tk.Canvas(self.root, width=600, height=600)
        self.page_canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Create a scroll bar for the listbox
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Words listbox
        self.words_listbox = tk.Listbox(
            self.root, width=40, justify=tk.RIGHT, font=("Arial", 14), yscrollcommand=scrollbar.set
        )
        self.words_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.words_listbox.yview)

        # Navigation buttons
        self.next_button = tk.Button(self.root, text="Next", command=self.next_page)
        self.next_button.place(x=500, y=560)
        self.prev_button = tk.Button(self.root, text="Previous", command=self.prev_page)
        self.prev_button.place(x=420, y=560)

        # Bind page click and shortcuts
        # self.page_canvas.bind("<Button-1>", self.on_page_click)
        self.bind_shortcut_key()

        # Display the initial page and words
        self.display_page_and_words()

    def display_page_and_words(self):
        """Display the current page image and its words."""
        if not (2 <= self.current_page <= 521):
            print("Page out of bounds.")
            return

        # Load and display the page image
        page_image_path = self.quran_pages[self.current_page - 2]
        self.page_image = Image.open(page_image_path)
        self.page_image.thumbnail((600, 600))  # Resize while preserving aspect ratio
        page_image_tk = ImageTk.PhotoImage(self.page_image)
        self.page_canvas.create_image(0, 0, anchor=tk.NW, image=page_image_tk)
        self.page_canvas.image = page_image_tk  # Keep reference to avoid garbage collection

        # Display page label
        page_label = tk.Label(self.root, text=f"Page: {self.current_page}")
        page_label.place(x=500, y=460)

        # Load words for the current page
        self.display_words()

    def display_words(self):
        """Fetch and display words for the current page."""
        self.words_listbox.delete(0, tk.END)  # Clear the listbox

        query = """
        SELECT wordindex, wordsno, rawword, x, y, width, surah, ayah 
        FROM wordsall 
        WHERE page_number2 = ?
        """
        cursor = self.db_connection.cursor()
        cursor.execute(query, (self.current_page,))
        word_data = cursor.fetchall()

        # Draw words and add to listbox
        for row in word_data:
            word = row["rawword"]
            start_x = int(row["x"] * self.page_image.width)
            start_y = int(row["y"] * self.page_image.height)
            width = int(row["width"] * self.page_image.width)

            self.words_listbox.insert(tk.END, f"{row['ayah']} : {word}")

            # Draw word marker on the page
            self.draw_colored_line(start_x, start_y, width, row["wordsno"])

    def draw_colored_line(self, start_x, start_y, width, wordsno):
        """Draw a colored line for the word on the page."""
        draw = ImageDraw.Draw(self.page_image)
        line_color = (255, 0, 0) if wordsno < 999 else (0, 0, 255)  # Red for wordsno < 999, blue otherwise
        draw.line([(start_x, start_y), (start_x + width, start_y)], fill=line_color, width=3)

        # Update the canvas image
        page_image_tk = ImageTk.PhotoImage(self.page_image)
        self.page_canvas.create_image(0, 0, anchor=tk.NW, image=page_image_tk)
        self.page_canvas.image = page_image_tk

    def next_page(self):
        """Navigate to the next page."""
        if self.current_page < len(self.quran_pages) + 1:
            self.current_page += 1
            self.display_page_and_words()

    def prev_page(self):
        """Navigate to the previous page."""
        if self.current_page > 2:
            self.current_page -= 1
            self.display_page_and_words()

    # def on_page_click(self, event):
    #     """Handle page click to update word coordinates."""
    #     x, y = event.x, event.y
    #     print(f"Clicked at coordinates: ({x}, {y})")

    #     selected_index = self.words_listbox.curselection()
    #     if selected_index:
    #         word_index = selected_index[0]
    #         print(f"Selected word index: {word_index}")
    #         # Update logic for word coordinates can be added here.

    def bind_shortcut_key(self):
        """Bind shortcut keys."""
        self.root.bind("n", lambda event: self.next_page())

    def run(self):
        """Run the app."""
        self.root.mainloop()


# Create and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuranBrowserApp(root)
    app.run()
