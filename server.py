import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!disconnect'

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(ADDR)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION]  connected")

    connected = True
    while connected:
        header = conn.recv(HEADER).decode(FORMAT)
        if header:
            header = int(header)
            msg = conn.recv(header).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f'[{addr}] is desconnected')
            print(f'[{addr}] $ {msg}')

    conn.close()



def start():
    server.listen(5)
    print(f"[SERVER] server is running on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")

print('[STARTING] server is starting')

start()