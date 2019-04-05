# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:17:06 2019

chatbot corpus comes from:
https://github.com/gunthercox/chatterbot-corpus

@author: whq672437089
"""
import generateResponse as gr
import preprocess as pp
import os
import socket
import sys

#Initialize question and responses for chatbot
content=""
workdir = os.path.dirname(os.path.abspath(__file__))

with open(workdir + "/corpus.txt") as infile:
    for line in infile:
        content=content+" "+line.lower()
qrDict=pp.generateConversationTurnDict(content)
index=0
for question,answer in qrDict.items():
    print("question is:"+question+', answer is'+answer+', index is:'+str(index))
    index+=1
    
pureQuestions=pp.pureQuestionsText(qrDict)
sentenceTokens=pp.generateSentenceTokens(pureQuestions)
index2=0
for question in sentenceTokens:
    print("index is:"+str(index2)+", question is:"+question)
    index2+=1
ql=[]
for question,response in qrDict.items():
    ql.append(question)

#Socket variables
botPort = 1234
botTCP = 1024
botName = "ROBO"

#Initialize socket connection
print("Starting friend chatbot...\n")

botSocket = socket.socket()
host = socket.gethostname()
ipAdd = socket.gethostbyname(host)
botSocket.bind((host, botPort))
print("Host: " + str(host) + " IP: " + str(ipAdd))

#Listen for incoming connection and accept connection
botSocket.listen(1)
print("Waiting for connection...\n")
connect, clientAdd = botSocket.accept()
print("Connection from " + str(clientAdd[0]) + "\n")
clientName = connect.recv(botTCP).decode()
print("Connected to " + str(clientName) + "\n")
connect.send(botName.encode())

#Start chat session
startMsg = "Hello, I am a chatbot and your friend. Type Bye to exit."
connect.send(startMsg.encode())
print(botName + ": " + startMsg + "\n")

#Chat loop
while True:
    msg = str(connect.recv(botTCP).decode())
    print(str(clientName) + ": " + msg + "\n")

    input = pp.sanitize_questions(msg.lower())
    if(input != "bye"):
        response = gr.generateResponse(input, sentenceTokens, qrDict, ql)
        print(botName + ": " + str(response) + "\n")
        connect.send(response.encode())
        sentenceTokens.remove(input)
    else:
        response = "Bye! Take care."
        print(botName + ": " + response + "\n")
        connect.send(response.encode())
        break