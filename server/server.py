import socket
import os
import jsonpickle

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

def get_id():
    id = "1"
    try:
        os.mkdir(str(id))
    except:
        pass
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
            if data == b'get_id':
                get_id()
                conn.sendto(b'test',addr)

            else:
                print("Client Says: " + data)
            #print ("Client Says: "+data)
            #conn.sendall("Server Says:hi")


     except Exception as e:
         print(e)


if __name__ == '__main__':
    main()