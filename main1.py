import kivy
from kivy.uix.carousel import Carousel
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
import subprocess
import glob
kivy.require('1.9.0')

class MyNewWidget(BoxLayout):
    def on_load(self, *args):
            x = 'D:/trusti/*.jpg'
            path = glob.glob(x)
            args[0].loop = True
            for y in path:
                u = Image(source=y)
                u.description = "Describing: " + y
                args[0].add_widget (u)
                print("loaded " + y)

    def on_clear(self, *args):
        if isinstance (args[0], Carousel):
            print ("clearing")
            args[0].clear_widgets()
            print ("cleared")
        if args[1]:
            args[1].text = "Cleared!"
            
    def on_run(self, *args):
        if args[0].current_slide:
            args[1].text = args[0].current_slide.description

    def on_current_slide(self, *args):
        if args[0].current_slide:
            args[1].text =  args[0].current_slide.source + " new slide "

class Lab1App(App):
    pass

if __name__ == '__main__':
    Lab1App().run()





