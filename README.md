# 310 ChatBot

## Assignment 2

### Introduction:
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

## Assignment 3

### Introduction:
This improved friend chatbot is based on the code from Assignment 2 and changes have been made to number of areas and some stayed the same. Chatbot processing of user input remains the same. The chatbot has been modified to represent the client-sever model and communicating using socket.
 
### Major Changes to code:
  •	main.py now acts as a sever to accept connections on port 1234 and receive messages from client on port 1024
  •	added client.py with GUI for client/another chatbot to connect to friend chatbot and communicate

### How to run the program:
  1.	Program requires Python 3.7 32-bit, NLTK, scikit-learn
      pip install -U scikit-learn
      pip install nltk
  2.	Launch command line, run main.py, and make note of the output IP address
  3.	Launch another command line, run client.py, enter the IP address and desired username when prompted
  4.	A client window will open and now users can talk to the friend chatbot
  5.	To end the program type “bye” and send, the client window will automatically close

### Features added:
  1. GUI
     1. Users now can chat with the chatbot with a simple and convenient GUI window
  2. New chatbot topic
     1. Interest – video game
     2. Users can now talk to chatbot about their video game interests
     3. Sample
         1. User: Do you like video games?
         2. ROBO: Of course I do.
         3. User: Do you play video game often?
         4. ROBO: Whenever no one is talking to me.
  3. Response to query outside of knowledge base
     1. Chatbot response added to user query that is outside knowledge base
     2. Randomised response and some will prompt user for another query
     3. Users will know when their input is not being understood by the chatbot and type something else
     4. Sample
        1. User: air plane
        2. ROBO: Your input keywords do not exist in my knowledge.
  4. Handle spelling mistakes
     1. Chatbot can now handle small spelling mistakes
     2. Users can now avoid the annoyance of getting an unintended response and must type again
     3. Sample
        1. User: What can you eat?
        2. ROBO: I consume ram, and binary digits.
        3. User: what can you eee
        4. ROBO: I consume ram, and binary digits.
  5. Language toolkits
     1. Completed in Assignment 2
     2. From sklearn.feature_extraction.text import TfidVectorizer
        1. Convert a collection of raw documents to a matrix of TF-IDF features
        2. Used on user input for similarity calculation
     3. From sklearn.metrics.pairwise import cosin_similarity
        1. Compute cosin similarity between samples
        2. Used in process of match user input to keys in the dictionary
     4. From nltk.stem import WordNetLemmatizer
        1. Finds matching word in WordNet
        2. Process user input
     5. Toolkits used to help process user inputs to better understand the user
 6. Conversation via sockets
     1. Any user or other chatbots on the same local network can talk to this chatbot when configured to use sockets and port 1234 and 1024
     2. Chatbot now acts like a server and clients or other chatbots can connect to it and communicate with it
