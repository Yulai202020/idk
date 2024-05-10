import socket, threading
n = 1024

def listen(client):
    while True:
        data = client.recv(1024)
        if not data:
            break
        msg = data.decode()

        print(msg)

def send(client):
    while True:
        try:
            client.connect(HOST)
        except: pass

        message = input("Enter smth : ")

        client.send(message.encode())

        print("Message sended.")


HOST = ("192.168.100.37", 9999)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Connected to", HOST)

client.connect(HOST)

listen_fn = threading.Thread(target=listen, args=(client,))
send_fn = threading.Thread(target=send, args=(client,))

listen_fn.start()
send_fn.start()

listen_fn.join()
send_fn.join()

client.close()