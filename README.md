# 310 ChatBot

Assignment 2

Introduction:
This is a simple chatbot program. The most fundamental theory that this program relies on is text similarity.

The following steps describe the logic of this program:
  •	Clean text, including remove punctuation, duplicate whitespace.
  • Divide text into multiple independent conversation turns.
  •	Based on such conversation turns, create a dictionary whose key is the question and value the response.
  •	Combine only questions, then tokenizing and lemmatization them.
  •	Vectorize those sentence tokens and compare the user input with them.
  •	Find the most similar question and use it as key to retrieve answer from training corpus.
  •	Output answer/response.

The training corpus used in our project comes from this [Repo](https://github.com/gunthercox/chatterbot-corpus)

Assignment 3

Introduction:
This improved friend chatbot is based on the code from Assignment 2 and changes have been made to number of areas and some stayed the same. Chatbot processing of user input remains the same. The chatbot has been modified to represent the client-sever model and communicating using socket.
 
Major Changes to code:
  •	main.py now acts as a sever to accept connections on port 1234 and receive messages from client on port 1024
  •	added client.py with GUI for client/another chatbot to connect to friend chatbot and communicate

How to run the program:
  1.	Program requires Python 3.7 32-bit, NLTK, scikit-learn
      pip install -U scikit-learn
      pip install nltk
  2.	Launch command line, run main.py, and make note of the output IP address
  3.	Launch another command line, run client.py, enter the IP address and desired username when prompted
  4.	A client window will open and now users can talk to the friend chatbot
  5.	To end the program type “bye” and send, the client window will automatically close

Features added:
  •	GUI
    o	Users now can chat with the chatbot with a simple and convenient GUI window
  •	 New chatbot topic
    o	Interest – video game
    o	Users can now talk to chatbot about their video game interests
    o	Sample
      	User: Do you like video games?
      	ROBO: Of course I do.
      	User: Do you play video game often?
      	ROBO: Whenever no one is talking to me.
  •	Response to query outside of knowledge base
    o	Chatbot response added to user query that is outside knowledge base
    o	Randomised response and some will prompt user for another query
    o	Users will know when their input is not being understood by the chatbot and type something else
    o	Sample
      	User: air plane
      	ROBO: Your input keywords do not exist in my knowledge.
  •	Handle spelling mistakes
    o	Chatbot can now handle small spelling mistakes
    o	Users can now avoid the annoyance of getting an unintended response and must type again
    o	Sample
      	User: What can you eat?
      	ROBO: I consume ram, and binary digits.
      	User: what can you eee
      	ROBO: I consume ram, and binary digits.
  •	Language toolkits
    o	Completed in Assignment 2
    o	From sklearn.feature_extraction.text import TfidVectorizer
      	Convert a collection of raw documents to a matrix of TF-IDF features
      	Used on user input for similarity calculation
    o	From sklearn.metrics.pairwise import cosin_similarity
      	Compute cosin similarity between samples
      	Used in process of match user input to keys in the dictionary
    o	From nltk.stem import WordNetLemmatizer
      	Finds matching word in WordNet
      	Process user input
    o	Toolkits used to help process user inputs to better understand the user
•	Conversation via sockets
    o	Any user or other chatbots on the same local network can talk to this chatbot when configured to use sockets and port 1234 and 1024
    o	Chatbot now acts like a server and clients or other chatbots can connect to it and communicate with it
