import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import subprocess
import pathlib
from pathlib import Path
from bs4 import BeautifulSoup
from tt import resetLink
from kivy.core.window import Window
Window.maximize() # fullscreen = True # size = (2500, 700)

def scrape_html_files(directory):
    # Create an empty list to store the results
    results = []

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            # Load the HTML file
            with open(os.path.join(directory, filename)) as f:
                soup = BeautifulSoup(f, 'html.parser')

            # Find all elements with the specified class
            elements = soup.find_all(class_='text-secondary group-hover:text-primary')

            # Loop through the elements and extract the content and href
            for element in elements:
                content = element.text
                href = element['href']
                results.append((content, href))

    return results


def playSeries(pathe):
    resetLink()
    t = ["C:/Users/bing/Desktop/mpv/mpv.exe", "--fs", "--fs-screen=0", "--loop-playlist" ]
    path1 = Path ('D:/htmlsource/' + pathe )
    sources = Path(path1).glob('*.html')
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
    

    




class DirectoryGrid(GridLayout):
    def __init__(self, path, **kwargs):
        super(DirectoryGrid, self).__init__(**kwargs)
        self.path = path
        self.cols = 3
        self.populate()
    
    def populate(self):
        print(os.listdir(self.path), "was apth")
        o = []
        o.extend(os.listdir(self.path))
        o.sort(key=str.lower)
    
        print (o)


        #for dir in os.listdir(self.path):
        for dir in o: #os.listdir(self.path):
            if os.path.isdir(os.path.join(self.path, dir)):
                btn = Button(text=dir)
                btn.bind(on_press=self.select_directory)
                self.add_widget(btn)
                
    def select_directory(self, instance):
        playSeries(instance.text)

class DirectoryApp(App):
    def build(self):
        return DirectoryGrid(path='D:/htmlsource')

if __name__ == '__main__':
    resetLink()
    DirectoryApp().run()