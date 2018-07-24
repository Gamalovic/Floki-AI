from __future__ import unicode_literals
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import random, re 
import spacy




nlp = spacy.load('en')


#--------------------------------------------------------------------------------------------------------------#

def Name_Entity(text) :
    doc = nlp(text.decode('utf8'))
    ## OR doc = nlp(text.decode('utf8'))
    Entities_labels=['PERSON','NORP','ORG','GPE','WORK_OF_ART','PRODUCT']
    Z_spacy = False
    # Find named entities, phrases and concepts
    for entity in doc.ents:
        if Z_spacy == True :
            break
        #print(entity.text, entity.label_)
        for w in Entities_labels:
            if entity.label_ == w: 
                result = entity.text 
                return result       
                #print(entity.text)
                Z_spacy = True 
    if Z_spacy == False :
        result = NLP(text)
        return result
        

#----------------------------------------------------------------------------------------------------------------#

def NLP(message) :
    #input
    #message = raw_input("Enter your message >> ")
    
    # work Tokenizing 
    #print(word_tokenize(message))
    message = word_tokenize(message)

    # defining stop words 
    #Minimizing probability 
    stop_words = set(stopwords.words("english"))

    filtered_sentence = []

    #filtering Method
    for w in message:
        if w not in stop_words:
            filtered_sentence.append(w)
    #print(filtered_sentence)
    if filtered_sentence != '' :
        result = filtered_sentence[0]
        
        #print(filtered_sentence[0])
        return result
    '''
    for x in filtered_sentence :
        new_message = new_message + x + ' ' 
    print(new_message) 
    '''
#Test
#result = Name_Entity(' you hello Mary mohamed asdbaksbd ')
#print(result)


#----------------------------------------------------------------------------------------------------------------------#
