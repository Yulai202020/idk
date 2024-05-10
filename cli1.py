import socket, threading

n = 1024
HOST = ("192.168.100.37", 10000)

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

        message = input("Enter message : ")

        if message == "":
            continue

        client.send(message.encode())
        print("Message sended.")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)

print("Connected to", HOST)

try:
    listen_fn = threading.Thread(target=listen, args=(client,))
    send_fn = threading.Thread(target=send, args=(client,))

    listen_fn.start()
    send_fn.start()

    listen_fn.join()
    send_fn.join()
except:
    exit()
finally:
    client.close()