import socket

bind_ip = "127.0.0.1"
bind_port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)
print(f"[*] Localizado en > {bind_ip} con el puerto >{bind_port}")

while True:
    client_socket, addr = server.accept()
    print(f"[*] Alguien se conecto: {addr[0]}:{addr[1]}")

    request = client_socket.recv(1024).decode()
    print(f"[*] mensaje > {request}")

    client_socket.send("si recibio".encode())

    client_socket.close()