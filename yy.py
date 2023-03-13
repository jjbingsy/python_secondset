from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import os

class ImagePopup(Popup):
    def __init__(self, image_path, **kwargs):
        super(ImagePopup, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.image = AsyncImage(source=image_path, allow_stretch=True)
        self.name = Label(text=os.path.basename(image_path))
        layout.add_widget(self.image)
        layout.add_widget(self.name)
        self.add_widget(layout)

class SeriesApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical')
        self.directories = os.listdir("C:/Users/bing/Desktop/bing1/")
        self.buttons = []
        for directory in self.directories:
            button = Button(text=directory, size_hint=(1, None), height=30)
            button.bind(on_press=self.show_images)
            self.buttons.append(button)
        self.root.add_widget(BoxLayout(orientation='horizontal', size_hint=(1, None), height=30, children=self.buttons))
        self.carousel = Carousel(direction='right')
        self.root.add_widget(self.carousel)
        return self.root

    def show_images(self, instance):
        images = []
        directory = os.path.join("d:/series", instance.text)
        for file in os.listdir(directory):
            if file.endswith(".jpg"):
                image_path = os.path.join(directory, file)
                images.append(ImagePopup(image_path))
        self.carousel.clear_widgets()
        for image in images:
            self.carousel.add_widget(image)

if __name__ == '__main__':
    SeriesApp().run()
