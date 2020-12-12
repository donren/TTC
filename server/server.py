import socket

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print (host , port)
while True:
 s.listen(1)
 conn, addr = s.accept()
 print('Connected by', addr)
 try:
        data = conn.recv(1024)
        print ("Client Says: "+data)
        conn.sendall("Server Says:hi")

 except:
       pass
