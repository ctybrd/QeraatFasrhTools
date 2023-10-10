from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os

class QuranApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        search_input = TextInput(hint_text="Search Quranic data")
        search_button = Button(text="Search")
        result_label = Label(text="Search results will be displayed here")

        layout.add_widget(search_input)
        layout.add_widget(search_button)
        layout.add_widget(result_label)

        return layout

# Set the graphics backend
os.environ['KIVY_METRICS_DENSITY'] = '2'
os.environ['KIVY_TEXT'] = 'pil'
os.environ['KIVY_IMAGE'] = 'pil'
os.environ['KIVY_WINDOW'] = 'sdl2'

if __name__ == '__main__':
    QuranApp().run()
