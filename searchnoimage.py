from pathlib import Path
import os
from tt import resetLink
from tt import parseTitle
from tt import read_file_to_list
from tt import resetLink


#file_path = 'paths.txt'
#paths = read_file_to_list(file_path)
#resetLink()
# Directory to store the soft links

resetLink()
link_dir = Path (read_file_to_list('softlinkdir.txt')[0])

x = Path(link_dir).glob('*')
for f in x:
    #print (f)
    if os.path.islink(f):
        #JPEG-DIRECTORY  AT "D:/trusti/" is still hardcodded
        filename = "D:/trusti/" + parseTitle( Path(f).stem) + ".jpg"
        k = Path (filename)
        if not k.exists():
            print ("No image:", Path(f).stem.upper())
        else:
            pass #print (k)

