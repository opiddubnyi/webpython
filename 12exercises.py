# number 1 & 2

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import socket

# url = str(input())
# host = url.split('/')
# print(host)
# cmd = f'GET {url} HTTP/1.0\r\n\r\n'
# counter = 0
# try:
#     mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     mysock.connect((host[2], 80))
#     cmd = cmd.encode()
#     mysock.send(cmd)
#
#
#     while True:
#         data = mysock.recv(512)
#         counter += len(data)
#         if not data:
#             break
#         if counter < 1000:
#             print(data.decode(), end='')
#
# except OSError:
#     print('Make sure URL is correct')
# except IndexError:
#     print('Make sure URL is correct')
# mysock.close()

# number 3


# url = str(input())
# file_handler = rq.urlopen(url)
# count = 0
#
# for line in file_handler:
#     for char in line:
#         count += 1
#     if count < 3000:
#         print(line.decode())

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = str(input('Enter URL - '))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
count = 0
tags = soup('p')
for tag in tags:
    count += 1
print(html.decode())