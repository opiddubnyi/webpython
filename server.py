import socket
import requests
import re
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = str(input())

my_socket.connect((url.split('/')[2], 80))

cmd = f'GET {url} HTTP/1.0\n\n'.encode()

my_socket.send(cmd)
file = []
while True:
    data = my_socket.recv(512)
    data = data.decode().split('\n')
    if data.count('Content-Length'):
        file.append(data)
    if not data:
        break

print(file[0])
my_socket.close()

# url = 'http://data.pr4e.org/intro-short.txt'
# resp = requests.get(url)
#
# print(resp.headers['Last-Modified'])
# print(resp.headers['ETag'])
# print(resp.headers['Content-Length'])
# print(resp.headers['Cache-Control'])
# print(resp.headers['Content-Type'])