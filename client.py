import socket

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!disconnect'

SERVER = '127.0.1.1'
PORT = 1234
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def try_connection():
    client.connect(ADDR)

try_connection()
connection = True

def recv_file():
    print('reciving')
    file_name = client.recv(1024).decode()
    file = client.recv(1024).decode()
    f = open(str(file_name), 'wt')
    f.write(file)
    f.close()
    print(file)    


def send_file():
    pirnt('sending')
    file_name = client.recv(1024).decode()
    print(f'got the file name{file_name}')

    file = open(file_name, 'rb')
    f = file.read()
    print(f)
    client.send(f)
    file.close()

while connection:
    msg = client.recv(1024).decode()
    print(msg)

    if msg == 'send':
        recv_file()
    elif msg == 'recv':
        send_file()