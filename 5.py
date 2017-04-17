#!/usr/bin/python3

import urllib.request
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
obj = urllib.request.urlopen(url).read()
unpickled = pickle.loads(obj)

for line in unpickled:
    for ch, num in line:
        print(ch*num, end='')
    print('')


