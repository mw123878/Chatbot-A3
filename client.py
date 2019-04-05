import socket
import sys
import time
import threading as th
import tkinter as tk

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

#Procedure to handle receive message with threading
def recvMsg():
    while True:
        msg = clientSocket.recv(clientTCP).decode()
        if msg != "Bye! Take care.":
            displayMsg = botName + ": " + msg
            msgDisplay.insert(tk.END, displayMsg)
            print(botName + ": " + msg + "\n")
            msgDisplay.see(msgDisplay.size())
        else:
            displayMsg = botName + ": " + msg
            msgDisplay.insert(tk.END, displayMsg)
            print(botName + ": " + msg + "\n")
            msgDisplay.see(msgDisplay.size())
            msgDisplay.insert(tk.END, "Closing window...")
            msgDisplay.see(msgDisplay.size())
            print("System exit...\n")
            
            time.sleep(1)
            window.quit()
            sys.exit(0)

#Procedure to handle sending message and bind to GUI element
def sendMsg(event = None):
        response = msgSend.get()
        msgSend.set("")

        clientSocket.send(response.encode())
        displayMsg = userName + ": " + response
        msgDisplay.insert(tk.END, displayMsg)
        print(userName + ": " + response + "\n")
        msgDisplay.see(msgDisplay.size())

#GUI
window = tk.Tk()
window.title("ROBO Friend Chatbot")
frame = tk.Frame(window)

#Chatbot message display area and scrollbar
scroll = tk.Scrollbar(frame)
msgDisplay = tk.Listbox(frame, height = 30, width = 60, yscrollcommand = scroll.set)
scroll.pack(side = tk.RIGHT, fill = tk.Y)
msgDisplay.pack(side = tk.LEFT, fill = tk.BOTH)
frame.pack()
scroll.config(command = msgDisplay.yview)

#Message typing textbox and send button
msgSend = tk.StringVar()
textbox = tk.Entry(window, width = 45, textvariable = msgSend)
textbox.bind("<Return>", sendMsg)
textbox.pack(side = tk.LEFT)
button = tk.Button(window, text = "Send", command = sendMsg)
button.pack(side = tk.RIGHT)

#Start thread to receive message
recvThread = th.Thread(target = recvMsg).start()

print("Starting GUI...\n")
window.mainloop()