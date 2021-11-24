import socket

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8820))

server_socket.listen(1)

(client_socket, client_address) = server_socket.accept()

client_data = client_socket.recv(1024)
print("Received: %s" % client_data)
client_socket.send('Hello ' + client_data + '!')

client_socket.close()
server_socket.close()