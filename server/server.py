import socket
import os

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
id = 0

def get_id():
    id += 1
    os.mkdir("..//data//{}".format(id))
    return id


print (host , port)
while True:
 s.listen(1)
 conn, addr = s.accept()
 print('Connected by', addr)
 try:
        data = conn.recv(1024)
        print(data)
        if data.decode() == 'get_id':
            g_id = get_id()
            conn.sendto(g_id.encode(),address=addr)
        else:
            print("Client Says: " + data)
        #print ("Client Says: "+data)
        #conn.sendall("Server Says:hi")

 except:
       pass
