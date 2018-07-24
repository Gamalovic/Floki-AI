from __future__ import unicode_literals
import spacy
import xml.etree.ElementTree as ET
import os

def Embedding_similarity(new_input):
    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = spacy.load('en')

    def Similarity(sentence1,sentence2):
        # Determine semantic similarities
        doc1 = nlp(sentence1)
        doc2 = nlp(sentence2)
        similarity=doc1.similarity(doc2)
        #print(similarity)
        return similarity

    def Comparing(similarity,n,sentence1,sentence2):
        number = similarity
        simi = Similarity(sentence1,sentence2)
        return n , simi
         
 

    tree = ET.parse(os.path.abspath(os.path.curdir)+'/acc/AIML/Similarity.xml')
    root = tree.getroot()

    doc = new_input  
    similarity = 0
    new_similarity = 0
    num = None 
    new_num = None 
    for n in range(4050) :   #4050
        num , similarity = Comparing(similarity,n,str(root[n][0].text),doc)
        if new_similarity < similarity :
            new_similarity = similarity 
            new_num = num 
    if new_num != None and new_similarity > 0.69 :
        return str(root[new_num][0].text)
    else :
        return None 
'''
    if num != None :
        new_num , new_simi = num , similarity
'''
    

'''
message='the fries were gross'
x=Embedding_similarity(message)
print(x)
'''


