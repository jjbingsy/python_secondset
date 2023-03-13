import requests
import lxml
from bs4 import BeautifulSoup
from pytube import Playlist, YouTube
import subprocess
from pathlib import Path


#SEOLHYUN vertical playlist
#retired
url = "https://youtube.com/playlist?list=PLqN5Awe3EmoCptmn0Qf5D-ZrtGGLg3Rvd"
url = "https://youtube.com/playlist?list=PLRthe34TNBvjC8O4Z6JQfUotdmDhKqdu6"
url = "https://youtube.com/playlist?list=PLB2soFiKVFG32Tfw0hWdhONZkldsbbV6L"
vlink = Playlist(url)


mpath = 'C:/Users/bing/Desktop/ioo/aoa'

p = Path(mpath)

files = set()
for i in p.iterdir():
    files.add( i.stem[-12:-1]) 

#print (files, len(files))

#print (pl.difference(files))


for e in vlink:
    url = e.split('?v=')[1]
    if url not in files:
        subprocess.run (["C:/ffmpeg/bin/yt-dlp.exe", e])
        print(url)




