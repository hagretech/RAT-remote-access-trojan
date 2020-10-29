import socket
import threading

# GLOBALS 
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!disconnect'

PORT = 7070
SERVER = '192.168.1.7'
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

# function to send files 
def send_file(conn):
    print('sending')
    file_name = input('Enter file name : ')
    conn.send(file_name.encode())

    file = open(file_name, 'rb')
    f = file.read()
    conn.send(f)
    file.close()

# function to recv files
def recv_file(conn):
    file_name = input('Enter file name : ')
    conn.send(file_name.encode())
    print('reciving')
    file = conn.recv(1024).decode()
    f = open(str(file_name), 'wt')
    f.write(file)
    f.close()
    print(file)    

# function that accept cmd commands and send it to the client 
def cmd(conn):
    active = True
    while active:
        command = input('command prompt > ')
        conn.send(command.encode())
        # checking if the command is exit and if so break the loop
        if command == 'exit':
            break
        # classifying all the responses in to 0 and 1
        res = conn.recv(24).decode()
        if res == '0':
            print('success')
        else :
            print('error')

# connection handler 
def handle_client(conn, addr):
    print(f"[NEW CONNECTION]  connected")
    connection = True
    while connection:
        massage = input('haha: ')
        conn.send(massage.encode())

        # checking the commands 
        if massage == 'end':
            conn.close()
            connection = False
            break
        elif massage == 'send':
            send_file(conn)
        elif massage == 'recv':
            recv_file(conn)
        elif massage == 'cmd':
            cmd(conn)

# connection initalizing function      
def start():
    server.listen(5)
    print(f"[SERVER] server is running on {SERVER}")
    while True:
        conn, addr = server.accept()
        handle_client(conn, addr)
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")

start()