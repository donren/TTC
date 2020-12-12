import socket
import os
import jsonpickle

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
id = 0

def get_id():
    id += 1
    print("debug")
    os.mkdir(str(id))
    return str(id)

def main():
    print (host , port)
    while True:
     s.listen(1)
     conn, addr = s.accept()
     print('Connected by', addr)
     try:
            data = jsonpickle.loads(conn.recv(1024).decode())
            print(data)
            print(addr[0])
            if data == b'get_id':
                g_id = get_id()
                conn.sendall(b'test',address=addr[0])
            else:
                print("Client Says: " + data)
            #print ("Client Says: "+data)
            #conn.sendall("Server Says:hi")

     except:
           pass

if __name__ == '__main__':
    main()