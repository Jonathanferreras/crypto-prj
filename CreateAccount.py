import socket
from PasswordHandler import *

def create_account(client):
    while True:

        client.send("Press 1 to create an account\nPress 2 to login\nPress 3 to exit")
        response = client.recv(1024)

        if response == '1':
            client.send("Let's create an account\n")

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
