import socket
import threading

# vars

HOST1 = ("192.168.100.37", 10000)
HOST2 = ("192.168.100.37", 9999)
sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.socket(socket.AF_INET, socket.SOCK_STREAM)]

# init

sockets[0].setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sockets[1].setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sockets[0].bind(HOST1)
sockets[1].bind(HOST2)

sockets[0].listen()
sockets[1].listen()


conn, addr = sockets[0].accept()
conn1, addr1 = sockets[1].accept()

# listeners

def listen_A():
    while True:
        req = ''

        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn1.sendall(data)

def listen_B():
    while True:
        req = ''

        while True:
            data = conn1.recv(1024)
            if not data:
                break
            conn.sendall(data)

if __name__ =="__main__":
    try:
        A = threading.Thread(target=listen_A)
        B = threading.Thread(target=listen_B)
    
        A.start()
        B.start()
    
        A.join()
        B.join()

    except: 
        exit()

    finally:
        conn.close()
        conn1.close()