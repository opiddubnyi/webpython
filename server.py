import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()

my_socket.send(cmd)

while True:
    data = my_socket.recv(512)
    if not data:
        break
    print(data.decode())
my_socket.close()
print('test')
