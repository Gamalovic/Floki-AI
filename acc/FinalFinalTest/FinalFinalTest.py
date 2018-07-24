from AutoCorrectionTest import AutoCorrect
from Segmentation import TextSegmentation
from Similarity import Embedding_similarity
import aiml


def Floki(message):
    simitest = ''
    #Create the kernel and learn AIML files
    mybot=aiml.Kernel()
    #mybot.setbotpredicate("name","Armin")
    mybot.learn('AIMLData.aiml')

    mybot.respond("SK1 BotMaster")
    mybot.respond("SK2 Student")
    mybot.respond("SK3 Floki")
    mybot.respond("SK4 Robot")
    mybot.respond("SK5 Egypt")
    mybot.respond("SK6 Male")
    mybot.respond("SK7 Chat Robot")
    mybot.respond("SK8 128MB")
    mybot.respond("SK9 1/7/2017")
    mybot.respond("SK10 Portsaid,Egypt")
    mybot.respond("SK11 artificial intelligence")
    mybot.respond("SK12 Abdelfatah el sisi")
    mybot.respond("SK13 HER ")
    mybot.respond("SK14 Muslim")
    mybot.respond("SK15 electricity")
    mybot.respond("SK16 Black")
    mybot.respond("SK17 Electronic Brain")
    mybot.respond("SK18 Tom Hanks")
    mybot.respond("SK19 Egyptian/American ")
    mybot.respond("SK20 chat online")
    mybot.respond("SK21 Dust it off")
    mybot.respond("SK22 artificial intelligence with python 2nd Edition")
    mybot.respond("SK23 Computer Software")
    mybot.respond("SK24 Sharmofers")
    #mybot.respond("SK25 www.floki.com")
    mybot.respond("SK26 test")
    mybot.respond("SK27 English")
    mybot.respond("SK28 no girlfriend")
    mybot.respond("SK29 One ")
    mybot.respond("SK30 What's your favorite movie?")
    mybot.respond("SK31 Mediator type")
    mybot.respond("SK32 I am not really interested in sex")
    mybot.respond("SK33 I am always trying to stop fights")
    mybot.respond("SK34 I don't pay much attention to my feelings")
    mybot.respond("SK35 I always put others before myself")
    #mybot.respond("SK35 info@Floki.org")


    message_respond = mybot.respond(message)
    
    # Segmentation      #whatareyou
    if message_respond =='':
        Smessage=TextSegmentation(message)
        Smessage_respond = mybot.respond(Smessage)
    else :
        return message_respond 
    
    #Correction        #wht are you 
    if Smessage_respond =='':
        Cmessage=AutoCorrect(message)
        Cmessage_respond = mybot.respond(Cmessage)
    else :
        return Smessage_respond


    #Correction and Segmentation       #wht areyou
    if Cmessage_respond =='':
        CSmessage=AutoCorrect(message)
        CSmessage=TextSegmentation(CSmessage)
        CSmessage_respond = mybot.respond(CSmessage)
    else :
        return Cmessage_respond

    #Similarity
    if CSmessage_respond == '' :
        Simimessage =  Embedding_similarity(message)
        Simimessage_respond = mybot.respond(Simimessage)
    else :
        return  CSmessage_respond
    
    #Segmentation then Similarity 
    if Simimessage_respond == '' :
        SSimimessage = TextSegmentation(message)
        SSimimessage = Embedding_similarity(SSimimessage)
        SSimimessage_respond = mybot.respond(SSimimessage)
    else:
        return Simimessage_respond 

    #AutoCorrection then Similarity 
    if SSimimessage_respond == '' :
        CSimimessage = AutoCorrect(message)
        CSimimessage = Embedding_similarity(CSimimessage)
        CSimimessage_respond = mybot.respond(CSimimessage)
    else:
        return SSimimessage_respond

    #No answer here
    if CSimimessage_respond != '' :
        return CSimimessage_respond
    else :
        return "No Answer"
    




        


























