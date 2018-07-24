from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
#from AutoCorrectionTest import AutoCorrect
#from Segmentation import TextSegmentation



def testNLTK(message) : 
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

    message = filtered_sentence
    #print(message) 

    #lemmatizing to adjective 
    lemmatizer = WordNetLemmatizer()
    Lemmatized_sentence = []
    for w in message:
        Lemmatized_sentence.append(lemmatizer.lemmatize(w, pos="a"))
    #print(Lemmatized_sentence)
    message = Lemmatized_sentence

    #Our References
    Reference_sentence = [ 'schedule','event' ]
    Z = True 

    Reference_found = []

    '''
    #Searching References 
    for w in message:
        if w in Reference_sentence:
            Reference_found.append(w)
            #Z = False 
    '''


    #Meaning vs References 
    Meaning_sentence = []
    if Z == True  : 
        for w in message :
            for syn in wordnet.synsets(w):
                for l in syn.lemmas():
                    Meaning_sentence.append(l.name())
     
        message1 = set(Meaning_sentence)
    #print (message1)
        for w in message1:
            if w in Reference_sentence:
                Reference_found.append(w)
    return Reference_found
 


def Filtering(message):
    
    Reference_found = testNLTK(message)
    if Reference_found == [] :
        return message 
    else :
        return Reference_found[0]
                     
   

# output=Filtering('schedule event')
# print(output)

























