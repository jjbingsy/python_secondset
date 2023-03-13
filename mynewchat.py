from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from os import listdir

class CarouselWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.directory = "C:/Users/bing/Desktop/bing1"

        # Create the dropdown menu with all the directories
        self.dropdown = Button(text="Choose a directory", size_hint_y=None, height=44)
        self.dropdown.bind(on_release=self.show_dropdown)
        self.add_widget(self.dropdown)

        # Create the carousel to display the images
        self.carousel = Carousel(direction="right", size_hint=(1, 0.9))
        self.add_widget(self.carousel)

        # Create the permanent button to display the name of the current image
        self.image_name = Button(text="", size_hint_y=None, height=44, disabled=True)
        self.add_widget(self.image_name)

    def show_dropdown(self, instance):
        # Popup with a list of directories to choose from
        content = BoxLayout(orientation="vertical")
        for directory in listdir(self.directory):
            btn = Button(text=directory, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.load_images(btn.text))
            content.add_widget(btn)

        popup = Popup(title="Choose a directory", content=content, size_hint=(0.5, 0.5))
        popup.open()

    def load_images(self, directory):
        # Load all the images in the selected directory and add them to the carousel
        self.dropdown.text = directory
        self.carousel.clear_widgets()
        for image_path in listdir(f"{self.directory}/{directory}"):
            if image_path.endswith(".jpg"):
                image = Image(source=f"{self.directory}/{directory}/{image_path}")
                self.carousel.add_widget(image)

                # Update the name of the current image
                self.image_name.text = image_path
                self.image_name.disabled = False
           # Close the popup after a directory is selected
        
class MyApp(App):
    def build(self):
        return CarouselWindow()

if __name__ == '__main__':
    MyApp().run()
