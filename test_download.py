import urllib.request, urllib.parse, urllib.error
import datetime

date = datetime.date.today()
url = str(input("enter url to download: "))

img = urllib.request.urlopen(url)
fhand = open(f'{date}-TV.epub', 'wb')
size = 0
while True:
    info = img.read(100000)
    if not info:
        break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()
