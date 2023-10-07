from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

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
if __name__ == '__main__':
    QuranApp().run()