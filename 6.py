#!usr/bin/python3

import re
import urllib.request
import zipfile
import os

def getNextFileName(currentFileName):
    nextFileName = ''
    content = zipFile.open(currentFileName).read()
    print(content)
    m = re.search('Next nothing is +(\d+)', str(content))
    if m is not None:
        print(m.group(1))
        return True, m.group(1)+'.txt'
    else:
        return False, nextFileName


url = 'http://www.pythonchallenge.com/pc/def/channel.zip'

file, headers = urllib.request.urlretrieve(url, 'channel.zip')
zipFile = zipfile.ZipFile(file, 'r')
content = zipFile.open('readme.txt').read()
m = re.search('start from (\d+)', str(content))
nextFileName = m.group(1)+'.txt'
print(nextFileName)
success = True
comments = b''
while success:
    comments += zipFile.getinfo(nextFileName).comment
    success, nextFileName = getNextFileName(nextFileName)
    print(nextFileName)
print(comments.decode("utf-8"))

zipFile.close()
urllib.request.urlcleanup()
os.remove(file)
