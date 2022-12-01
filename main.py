from PIL import Image
from pillow_heif import register_heif_opener
import glob
from pathlib import Path
from re import search, IGNORECASE
from os import remove
import sys
register_heif_opener()

def convert_files(p, input1, input2):
    p = Path(p)

    for imgP in p.rglob('*'+input1):
        img = Image.open(imgP)
        img.convert()
        img.save(imgP.with_suffix(input2))
        remove(imgP)

if __name__ == "__main__":
    print("Enter Folder Path of file(s) to convert")
    inputPath = input()
    print("Enter current image extension\nEX:(.HEIC)")
    inputExt1 = input()
    print("Enter image extension you want\nEX:(.JPEG)")
    inputExt2 = input()

    convert_files(inputPath, inputExt1, inputExt2)

    '''inputPath = sys.argv[1]
    inputExt1 = sys.argv[2]
    inputExt2 = sys.argv[3]

    convert_files(*sys.argv[1:])'''