from NLP import testNLTK
from AutoCorrectionTest import AutoCorrect
from Segmentation import TextSegmentation

#input
message = input("Enter your message >> ")
Reference_found = testNLTK(message)
#for w in Reference_found :
    #print (w)

if Reference_found == []:
    newmessage = AutoCorrect(message)
    #print newmessage
    newReference_found = testNLTK(newmessage)
    if newReference_found == [] :
        newmessage = TextSegmentation(message)
        newReference_found = testNLTK(newmessage)
        for w in newReference_found:
            print(w)
    else :
        for w in newReference_found:
            print(w)
else : 
    for w in Reference_found : 
        print(w)
