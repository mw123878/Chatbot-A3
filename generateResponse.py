# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:03:35 2019

@author: whq672437089
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from nltk.stem import WordNetLemmatizer
import random

#for a given sentence,return a lemmatized sentence
def lemTokens(tokens):
    lemmatizer=WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]

def generateResponse(userInput,sentences,askResponseDict,ql,similarityThredhold=0.7):
    #prevent bad input
    if ((similarityThredhold>1) or (similarityThredhold<0)):
        similarityThredhold=0.5
    sentences.append(userInput)
    #vetorize sentences and userinput for fllowing similarity calculation
    vertorizedSentences=TfidfVectorizer(tokenizer=lemTokens,stop_words='english').fit_transform(sentences)
    vals = cosine_similarity(vertorizedSentences[-1], vertorizedSentences)
    #find index of sentences that has highest similarity with input
    valsWithoutLast=vals[0,:-1]
    idx=np.argmax(valsWithoutLast,axis=0)
    #return response
    if(vals[0][idx]<similarityThredhold):
        response = ["Your input keywords do not exist in my knowledge.", "Sorry, I do not understand.", "Sorry, KnowledgeOutOfBondsException, please type again.", "Sorry, I cannot comprehend.", "What is this? ROBO has no knolwedge of this, please type something else."]
        resIndex = random.randint(0, 4)
        robotResponse = response[resIndex]
        return robotResponse
    else:
        question=ql[idx]
        print("matched question from database: "+question)
        robotResponse =''+askResponseDict.get(question)
        return robotResponse