from .AutoCorrectionTest import AutoCorrect
from .Segmentation import TextSegmentation
from .Similarity import Embedding_similarity
import aiml
import os
import sys


def Floki(message):
    simitest = ''
    # Create a Kernel object.
    mybot = aiml.Kernel()

    # When loading an AIML set, you have two options: load the original
    # AIML files, or load a precompiled "brain" that was created from a
    # previous run. If no brain file is available, we force a reload of
    # the AIML files.
    brainLoaded = False
    forceReload = False
    while not brainLoaded:
        if forceReload or (len(sys.argv) >= 2 and sys.argv[1] == "reload"):
	    # Use the Kernel's bootstrap() method to initialize the Kernel. The
	    # optional learnFiles argument is a file (or list of files) to load.
	    # The optional commands argument is a command (or list of commands)
	    # to run after the files are loaded.
            mybot.bootstrap(learnFiles=os.path.abspath(os.path.curdir)+'/acc/AIML/std-startup.xml', commands="load aiml b")
            brainLoaded = True
	    # Now that we've loaded the brain, save it to speed things up for
	    # next time.
            mybot.saveBrain(os.path.abspath(os.path.curdir)+'/acc/AIML/standard.brn')
        else:
	    # Attempt to load the brain file.  If it fails, fall back on the Reload
	    # method.
            try:
		# The optional branFile argument specifies a brain file to load.
                mybot.bootstrap(brainFile = os.path.abspath(os.path.curdir)+'/acc/AIML/standard.brn')
                brainLoaded = True
            except:
                forceReload = True


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
        Simimessage_respond = ''
        if Simimessage != None :
            Simimessage_respond = mybot.respond(Simimessage)
    else :
        return  CSmessage_respond
    
    #Segmentation then Similarity 
    if Simimessage_respond == '' :
        SSimimessage = TextSegmentation(message)
        SSimimessage = Embedding_similarity(SSimimessage)
        SSimimessage_respond = ''
        if SSimimessage != None  :
            SSimimessage_respond = mybot.respond(SSimimessage)
    else:
        return Simimessage_respond 

    #AutoCorrection then Similarity 
    if SSimimessage_respond == '' :
        CSimimessage = AutoCorrect(message)
        CSimimessage = Embedding_similarity(CSimimessage)
        CSimimessage_respond = ''
        if CSimimessage != None : 
            CSimimessage_respond = mybot.respond(CSimimessage)
    else:
        return SSimimessage_respond

    #No answer here
    if CSimimessage_respond != '' :
        return CSimimessage_respond
    else :
        return "No Answer"
    




        


























