import socket
import sys

sys.dont_write_bytecode = True

def login(client, username, password):
    client.send("Login\n")

    while True:
        client.send("Enter your username:")
        existing_username = str(client.recv(1024))

        if existing_username == username:
            while True:
                client.send("Enter your password:")
                existing_password = str(client.recv(1024))

                if existing_password == password:
                    client.send("You are logged in!\n\n")
                    break
                else:
                    client.send("Incorrect password. Try again.\n")
            break
        else:
            client.send("Incorrect username or doesn't exist. Try again.\n")
