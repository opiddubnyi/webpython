import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
new_socket.connect((HOST, PORT))
new_socket.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = new_socket.recv(5120)
    if len(data) < 1: break
    # time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

new_socket.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos + 4:]
file_handler = open("stuff.jpg", "wb")
file_handler.write(picture)
file_handler.close()
