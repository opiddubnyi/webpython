# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = str(input('enter url: '))
count = int(input('enter count: '))
pos = int(input('enter position: '))

# Retrieve all of the anchor tags
for _ in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    array = []
    tags = soup('a')
    for tag in tags:
        array.append(tag.get('href', None))
    url = array[pos-1]


print(array[pos-1].split('/')[3].split('_')[2].split('.')[0])