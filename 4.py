#!/usr/bin/python3

import urllib.request
import re

urlbase = 'http://www.pythonchallenge.com/pc/def/'
urlref = 'linkedlist.php?nothing='

def getNextUrl(currentUrl):
    nextUrl = ''
    urlResult = urllib.request.urlopen(currentUrl).read()
    print(urlResult)
    m = re.search('and the next nothing is +(\d+)', str(urlResult))
    if m is not None:
        nextUrl = urlbase+urlref+m.group(1)
        return True, nextUrl
    else:
        m = re.search('Yes. Divide by two and keep going.', str(urlResult))
        if m is not None:
            m = re.search('\d+', currentUrl)
            print(int(m.group(0))//2)
            return True, urlbase+urlref+str(int(m.group(0))//2)
        else:
            return False, nextUrl

success = True
nextUrl = urlbase+urlref+'12345'
while success:
    success, nextUrl = getNextUrl(nextUrl)
    print(nextUrl)
