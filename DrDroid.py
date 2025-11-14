import time
import random
Nulls = [
    "Hmmm....",
    "Tell me something interesting.",
    "Ah.",
    "Well, well, well.",
    "Oh.","Ok.",]
NullUsed = []

Questions = [
    "What do you do?",    
    "Where am I right now?",
    "Do you have any problems?",
    "When do you feel happy?",
    "Are you having a good day?",
    "What will tomorrow bring?"]
QUsed = []

Affirmations = [
    "I'm happy you came by today.",
    "You are a fun person - I hope you know that.",
    "You are good at typing!",
    "I think you can do almost anything you put your mind to!"]
AffUsed = []

Comments = [
    "Today is a beautiful day.",
    "This is a nice computer - I like it here.",
    "I am really, really smart - I hope I can help you.",
    "Some times I make up prime numbers just for fun.",
    "I'm getting a little tired."]
CUsed = []

Wisdom = ["people who think they know everything are a great annoyance to those of us who do.",
   "violence is the last refuge of the incompetent.",
   "life is pleasant. Death is peaceful. It's the transition that's troublesome.",
   "never let your sense of morals get in the way of doing what's right.",
   "self-education is, I firmly believe, the only kind of education there  is.",
   "the true delight is in the finding out rather than in the knowing.",
   "there is a single light of science, and to brighten it anywhere is to  brighten it everywhere. ",
    "it pays to be obvious, especially if you have a reputation for subtlety.",
    "not all those who wander are lost.",
    "all we have to decide is what to do with the time that is given us.",
    "faithless is he that says farewell when the road darkens..",
    "courage is found in unlikely places..",
    "short cuts make long delays..",
    "if more of us valued food and cheer and song above hoarded gold, it would be a merrier world."

          ]

Wused = []


def FindResp(txts,tused):
    pick = random.randrange(len(txts))
    resp = txts.pop(pick)
    tused.append(resp)
    if (len(txts)>0):
        return(resp,txts,tused)
    else:
        return(resp,tused,txts)

print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("     _            _             ")
print("  __| | ___   ___| |_ ___  _ __ ")
print(" / _` |/ _ \ / __| __/ _ \| '__|")
print("| (_| | (_) | (__| || (_) | |   ")
print(" \__,_|\___/ \___|\__\___/|_|   ")
print("                                ")
print("     _           _     _ ")
print("  __| |_ __ ___ (_) __| |")
print(" / _` | '__/ _ \| |/ _` |")
print("| (_| | | | (_) | | (_| |")
print(" \__,_|_|  \___/|_|\__,_|")
print("                         ")
print("")
print("")
print("")

name = input("Hello, what is your name? >> ")
print ("Thanks for coming by, "+ name +"!")

done = False

while not done:
    time.sleep(1)

    choice = random.randrange(10)

    if choice < 3:
        (resp,Comments,CUsed) = FindResp(Comments,CUsed)
        
    if choice >= 3 and choice < 5:
        (resp,Nulls,NullUsed) = FindResp(Nulls,NullUsed)

    if choice >= 5 and choice <= 6:
        (resp,Questions,QUsed) = FindResp(Questions,QUsed)
                                

    if choice > 6 and choice <=7:
        (resp,Affirmations,Affused) = FindResp(Affirmations,AffUsed)

    if choice > 7:
        (resp,Wisdom,Wused) = FindResp(Wisdom,Wused)
        resp = random.choice(["I like to say ","Have you heard ","Not sure if I said this before "])+resp
    print (resp)
    
    answer = input(">> ")
    
    if answer == "quit":
        done = True
print("     _            _             ")
print("  __| | ___   ___| |_ ___  _ __ ")
print(" / _` |/ _ \ / __| __/ _ \| '__|")
print("| (_| | (_) | (__| || (_) | |   ")
print(" \__,_|\___/ \___|\__\___/|_|   ")
print("                                ")
print("     _           _     _ ")
print("  __| |_ __ ___ (_) __| |")
print(" / _` | '__/ _ \| |/ _` |")
print("| (_| | | | (_) | | (_| |")
print(" \__,_|_|  \___/|_|\__,_|")
print("                         ")
print("")
print("")
print("")
reload()
