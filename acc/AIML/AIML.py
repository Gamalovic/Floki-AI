import aiml
import os
# Create the kernel and learn AIML files
mybot=aiml.Kernel()
#mybot.setbotpredicate("name","Armin")

mybot.learn(os.path.abspath(os.path.curdir)+'/acc/AIML/AIMLData.aiml')

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

while True:
    message = input("Enter your message >> ")
    if message == "quit":
        exit()
#   elif message == "save":
 #       kernel.saveBrain("bot_brain.brn")
    else:
        print(mybot.respond(message))
