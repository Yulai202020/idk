import socket
import threading

# vars

clients_count = 2

HOST1 = ("192.168.100.37", 10000)

sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sck.bind(HOST1)
sck.listen()

# listeners

def handle(id_):
    while True:
        req = ''

        while True:
            data = list_of_conns[id_][0].recv(1024)
            if not data:
                break

            for i in range(count):
                if i == id_:
                    continue
                list_of_conns[i][0].sendall(data)

list_of_conns = []

count = 0
while True: 
    conn, addr = sck.accept()
    list_of_conns.append((conn, addr))
    user_thread = threading.Thread(target=handle, args=(count,))
    user_thread.start()
    count+=1