import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!disconnect'

PORT = 1234
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(ADDR)
server.bind(ADDR)

def send_file(conn):
    file_name = input(' Enter file name : ')
    conn.send(file_name.encode())
    file = open(file_name, 'rb')
    f = file.read()
    conn.send(f)
    file.close()


def handle_client(conn, addr):
    print(f"[NEW CONNECTION]  connected")
    connection = True
    while connection:
        massage = input('haha: ')
        conn.send(massage.encode())
        if massage == 'end':
            conn.close()
            connection = False
        elif massage == 'send':
            send_file(conn)

        
def start():
    server.listen(5)
    print(f"[SERVER] server is running on {SERVER}")
    while True:
        conn, addr = server.accept()
        handle_client(conn, addr)
        print(f"[ACTIVE CONNECTIONS] {threadin