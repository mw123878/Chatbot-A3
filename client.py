import socket
import sys
import time

#Ask user to input chatbot IP and user name
botIP = str(input("Enter chatbot IP address: "))
userName = str(input("Enter username to display: "))

#Connect to chatbot
clientSocket = socket.socket()
botPort = 1234
print("Connecting to chatbot at " + botIP + "\n")
clientSocket.connect((botIP, botPort))
print("Connected...\n")

#Send username to chatbot and receive chatbot name
clientTCP = 1024
clientSocket.send(userName.encode())
botName = clientSocket.recv(clientTCP).decode()

#Chat loop
while True:
    msg = clientSocket.recv(clientTCP).decode()
    print(botName + ": " + msg + "\n")
    
    response = str(input(userName + ": "))
    if response.lower() == "bye":
        clientSocket.send(response.encode())
        print(userName + ": " + response + "\n")
        msg = clientSocket.recv(clientTCP).decode()
        print(botName + ": " + msg + "\n")
        break
    else:
        clientSocket.send(response.encode())