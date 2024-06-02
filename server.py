import socket
import threading
import queue
# vars

clients = {}

HOST1 = ("192.168.100.37", 10000)

sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sck.bind(HOST1)
sck.listen()

list_of_conns = []

def send(data, nickname):
    global clients

    for i in list(clients.keys()):
        if i == nickname:
            continue

        end = '\n' + data.decode()

        clients[i].sendall(end.encode())

def handle(nickname):
    global clients

    while True:
        data = b''
        try:
            data = clients[nickname].recv(1024)
        except:
            del clients[nickname]
            break

        if not data:
            break

        send(data, nickname)

count = 0
while True:
    conn, addr = sck.accept()

    conn.send(b'NICK')
    nickname = conn.recv(1024).decode()

    while nickname in clients:
        conn.send(b'ER_NICKNAME_IS_EXITS')
        nickname = conn.recv(1024).decode()

    clients[nickname] = conn

    user_thread = threading.Thread(target=handle, args=(nickname,))
    user_thread.start()
    count+=1