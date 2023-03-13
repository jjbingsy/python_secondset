import os
from pathlib import Path
#import webp
from PIL import Image

folder = "d:/trustwebp"
os.chdir(folder)
for file in os.listdir():
    if file.endswith(".webp"):
        fn = Path(file).stem
        print (fn)
        with Image.open(file) as im:
            print (file)
        #     # Save the image as .jpg
            im.save(fn + '.jpg')


