import socket, threading, time

n = 1024
HOST = ("192.168.100.37", 10000)

nickname = input("Enter your nickname: ")

while len(nickname) >= 1024:
    print("nickname too big.")
    nickname = input("Enter your nickname: ")

def listen(client):
    global nickname
    while True:
        data = client.recv(1024)
        if not data:
            break

        msg = data.decode()

        if msg == "ER_NICKNAME_IS_EXITS":
            print("Nickname is exits.")
            nickname = input("Enter your nickname: ")
            client.sendall(nickname.encode())
        elif msg == "NICK":
            client.sendall(nickname.encode())
        else:
            print(msg)

def send(client):
    while True:
        message = input("Enter message: ")

        if message == "":
            continue

        formated = f"{nickname}: {message}"
        client.send(formated.encode())

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