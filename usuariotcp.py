import socket
target_host = "127.0.0.1"
target_port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))

client.send("pto el que lo lea".encode())

response = client.recv(4096)
print(response)
client.close()