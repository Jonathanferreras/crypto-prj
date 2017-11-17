import socket
from PasswordHandler import *

def create_account(client):
    while True:
        client.send("Enter a username:")
        username = str(client.recv(1024))

        if username != "":
            while True:
                client.send("Enter a password:")
                password = str(client.recv(1024))

                if pw_check(password):
                    client.send("Account created!\n\n")
                    break
                else:
                    client.send("Please enter a valid password.\n")
            break
        else:
            client.send("Please enter a valid username.\n")

    return username, password
