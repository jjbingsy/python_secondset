import os
import datetime
import pathlib
from pathlib import Path
import shutil
import sqlite3
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
import subprocess
import pathlib
from pathlib import Path
from bs4 import BeautifulSoup
from tt import resetLink


import kivy
from kivy.app import App
kivy.require('1.9.0')


def playSeries(pathe):
    
    t = ["C:/Users/bing/Desktop/mpv/mpv.exe", "--fs", "--fs-screen=0", "--loop-playlist" ]
    #path1 = Path ('D:/htmlsource/' + pathe )
    sources = pathe.iterdir()
    myset = set()
    for source in sources:
        if source.exists():
            #contents = ''
            with open(source, mode="r", encoding='utf-8') as f:
                #soup = BeautifulSoup(f, 'lxml')  D:\htmlsource\kkaede\k1.html
                contents = f.read() #print (source)#, f.read_text())
            soup = BeautifulSoup(contents, 'html.parser')
            elements = soup.find_all(class_='text-secondary group-hover:text-primary')

            # Loop through the elements and extract the content and href
            for element in elements:
                content = element.text
                href = element['href']
                txt = content.split()[0].lower()
                myset.add(txt)
    mylist = list (myset)
    mylist.sort()
    for txt in mylist:
        files = Path("C:/Users/bing/Desktop/link").glob ( txt + "*")
        for ff in files:
            print (ff)
            t.append (ff)

    #App.get_running_app().stop()
    subprocess.run (t)



#hs = {y:y * y for y in range(1,  10, 2)}


#h = {y:x for x,y in hs.items() }

#print (h)

#for i in h.items():
 #   print (i)

class RV(RecycleView):
    def __init__(self, **kargs):
        super().__init__(**kargs)
        p = Path("D:/htmlsource")



        self.data = [{"address": x} for x in p.iterdir()]
        #self.data = [{'name': "No. " + str(i), "address": "in your face " + str(i)} for i in range(20) ]

#class Post(Button):
#    name = StringProperty('')
#<Post>:
#    text: self.name

class MyBox (BoxLayout):
    #name = StringProperty('')
    address = ObjectProperty('')

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.text = "buffer"

    def on_press (self, *args):
        playSeries (self.address)
        

        

#class MyTrueWidget(FloatLayout):
#    def __init__(self,gT1='default' , **kargs):
#        super().__init__(**kargs)
#        b1 = Button(text=gT1, pos_hint={'x': 0, 'center_y': .5}, size_hint=(.49, 1))
#        b2 = Button(text="2", pos_hint={'right': 1, 'center_y': .5}, size_hint=(.49, 1))
#        self.add_widget(b1)
#        self.add_widget(b2)
    
class MyLab2App(App):
    pass        

if __name__ == '__main__':
    resetLink()
    MyLab2App().run()
