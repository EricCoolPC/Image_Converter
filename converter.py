from PIL import Image
from pillow_heif import register_heif_opener
import glob
from pathlib import Path
from re import match, search
from os import remove

register_heif_opener()

p = Path('C:/Users/eversaw/Pictures/test/burger')

for imgP in p.rglob('*.heic'):
    regex = search(r'^.*(?=(\.HEIC))|^.*(?=(\.heic))', imgP.name)
    fileName = regex.group(0)
    
    newPath = Path()
    i = 0
    for part in imgP.parts:
        if(i < len(imgP.parts) - 1):
            newPath = newPath.joinpath(part)
        i += 1

    newPath = newPath.joinpath(fileName+".jpeg")

    img = Image.open(imgP)
    img.convert()
    img.save(newPath)
    remove(imgP)