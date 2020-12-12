import socket
import jsonpickle
host = "192.168.178.23"
port = 12345                   # The same port as used by the server

def send_to_server(msg):
    msg = jsonpickle.dumps(msg)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(msg.encode())
    s.close()
    pass