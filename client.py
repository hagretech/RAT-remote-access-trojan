import socket

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!disconnect'

SERVER = '127.0.1.1'
PORT = 5050
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)

    msg_length = len(message)
    header = str(msg_length).encode(FORMAT)
    header +=  b' ' * (HEADER - len(header))
    print(header)
    client.send(header)
    client.send(message)


send('hahhha kira')
send('boom boom boom')
send(DISCONNECT_MESSAGE)