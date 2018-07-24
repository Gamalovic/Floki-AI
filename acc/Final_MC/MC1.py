
from MC2 import Name_Entity
import random, re 

###MAAAAAAAAAAAAAAAAAAAIIIIIIIIIIIIIIIIIIIIIINNNNNNNNNNNNNN
#-----------------------------------------------------------------------------------------------------#

def MarkovChain(startWord):

    #rep means reply / curr = current 
    #Reading Reference file and generate syntax 
    def testMarkov(startword):
        replib = {}
        addToLib('MCFile.txt' , replib)
        return makeReply(startword, replib)



    def addToLib(filename , currlib):
        f = open(filename , 'r')
        #job_titles = [line.decode('utf-8').strip() for line in title_file.readlines()]
        words = re.sub("\n","\n",f.read()).split(' ')
        curr = 0 
        while curr < len(words) - 1:
        #looping through all words including \n in this text generated
            currword = words[curr].lower()
            nextword = words[curr + 1].lower()
            if currword in currlib.keys() : 
                #if we have seen this word anytime before 
                if nextword in currlib[currword].keys():
                    #if we have seen the sequence currword -> nextword before 
                    currlib[currword][nextword] += 1 
                else:
                    # have not seen sequence currworld -> nextword before 
                    currlib[currword][nextword] = 1 
            else :
                # have not seen this word before 
                currlib[currword] = {nextword : 1}
            curr += 1
        # change counts to percentage 
        for key in currlib.keys(): 
            # for each word 
            keytotal = 1 
            for probkey in currlib[key].keys():
                keytotal += currlib[key][probkey]
            for probkey in currlib[key].keys():
                currlib[key][probkey] = currlib[key][probkey]/keytotal 
        return currlib 





    def markov_next(currentword , replib): 
        if currentword not in replib.keys():
            return random.choice(replib.keys())
        else :
            wordprobs = replib[currentword]
            randprob = random.uniform(0.0,1.0)
            currentprob = 0.0 
            for key in wordprobs : 
                currentprob = currentprob + wordprobs[key]
                if randprob <= currentprob :
                    return key 
	    return random.choice(replib.keys())


    #generate word by word 
    def makeReply(startword, replib):
        reply,current, w = '',startword,0 
        while w < 10 :
            reply = reply + current + ' ' 
            #initializing 9 next words 
            current = markov_next(current,replib) 
            w = w +1
        return reply




    #let's start
    #startWord = raw_input(" what do you want to start ? \n "  )
    message =  testMarkov(startWord)
    #print message
    #print "****\n"
    return message 
 


#------------------------------------------------------------------------------------------------------------#



def LastPhase(message):
    result = Name_Entity(message)
    new_result = MarkovChain(result.encode('utf8'))
    return new_result


#-------------------------------------------------------------------------------------------------------------#

message = raw_input("Say Something \n "  )
LastReply = LastPhase(message)
print(LastReply)
