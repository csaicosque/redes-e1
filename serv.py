import socket

HOST = '127.0.0.1'
PORT = 65001

files = ['arquivo1', 'arquivo2', 'arquivo3', 'arquivo4']

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
print('The server is ready to receive')
while True:
    data, client = s.recvfrom(4096)

    print(client, data)

    data = data.decode()

    if data in files:
        s.sendto('ok'.encode(), client)
    else:
        s.sendto('not ok'.encode(), client)
