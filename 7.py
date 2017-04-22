#!usr/bin/python3

import urllib.request
from PIL import Image
import os

url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
imageFile, headers = urllib.request.urlretrieve(url, 'oxygen.png')
img = Image.open(imageFile)
print(img.getbands())
pixels = img.load()

imgWidth, imgHeight = img.size
for h in range (0, imgHeight):
    print('')
    for w in range(0, imgWidth):
        r, g, b, a = pixels[w,h]
        if r == g == b:
            print(chr(r), end='')

nextLevel = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for c in nextLevel:
    print(chr(c), end='')

os.remove(imageFile)
