import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import platform
import lxml
import bs4

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Hello, World!')
        layout.add_widget(self.label)
        button = Button(text='Click me')
        button.bind(on_press=self.update_label)
        layout.add_widget(button)
        return layout

    def update_label(self, instance):
        self.label.text = 'You pressed the button'

if __name__ == '__main__':
    MyApp().run()


def display_python_version():
    version = platform.python_version()
    print(f"Python version: {version}")

display_python_version()
