import urllib.request, urllib.parse, urllib.error
import ssl
import json


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'https://py4e-data.dr-chuck.net/comments_1245985.json'

data = urllib.request.urlopen(url, context=ctx).read()
eat = json.loads(data)
print(eat)
sum = 0
for each in range(len(eat['comments'])):
    sum += (eat['comments'][each]['count'])
print(sum)
