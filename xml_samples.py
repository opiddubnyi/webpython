import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'https://py4e-data.dr-chuck.net/comments_1245984.xml'

data = urllib.request.urlopen(url, context=ctx).read().decode()
tree = ET.fromstring(data)
sum = 0

counts = tree.findall('comments/comment')

for comment in counts:
    sum += int(comment.find('count').text)

print(sum)