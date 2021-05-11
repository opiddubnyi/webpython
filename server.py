import socket
import requests
import re
# my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# my_socket.connect(('data.pr4e.org', 80))
#
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
#
# my_socket.send(cmd)
#
# while True:
#     data = my_socket.recv(512)
#     if not data:
#         break
#     print(data.decode())
# my_socket.close()

url = 'http://data.pr4e.org/intro-short.txt'
resp = requests.get(url)

print(resp.headers['Last-Modified'])
print(resp.headers['ETag'])
print(resp.headers['Content-Length'])
print(resp.headers['Cache-Control'])
print(resp.headers['Content-Type'])