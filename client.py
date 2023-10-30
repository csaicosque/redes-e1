import socket

HOST = '127.0.0.1'
PORT = 65001

arq = input('Enter the file name: ')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST, PORT))
s.sendall(arq.encode())
data = s.recv(4096).decode()
if data.startswith('ok'):
    print('Here what you search: ', data)
else:
    print(data)
