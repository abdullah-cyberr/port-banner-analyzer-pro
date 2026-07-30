import socket

HOST = "127.0.0.1"
PORT = 2222

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Listening on {HOST}:{PORT}")

while True:
    client, address = server.accept()

    print(f"Connection from {address}")

    banner = b"SSH-2.0-OpenSSH_9.0 Ubuntu-3ubuntu0.6\r\n"

    client.send(banner)

    client.close()