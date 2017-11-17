import socket
import sys

def connect(server):
    host = "127.0.0.1"
    port = 7777
    server.connect((host, port))
    server.sendall("Client connecting")


if __name__ == '__main__':
    server = socket.socket()
    connect(server)

    while True:
        response = server.recv(1024)
        print response
        if response == "Goodbye":

            server.close()
            sys.exit()
        else:
            data = raw_input()

            server.sendall(data)
