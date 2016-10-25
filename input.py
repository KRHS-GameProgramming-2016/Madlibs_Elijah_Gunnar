def isSwear(word):
    swearList = ["poop",
                 "pee",
                 "cunt",
                 "bitch",
                 "ass",
                 "pink sock",
                 "tits",
                 "canadian pipeline",
                 "pissing",
                 "fuck",
                 "fucking",
                 "fucked",
                 "fuck'd",
                 "fucker",
                 "fuckers",
                 "motherfucker",
                 "motherfuckers",
                 "motherfucking",
                 "fuckmothering",
                 "screw you",
                 "rimjob"
                 "pussy"
                 "f u c k"
                 "anal", 
                 "omg", 
                 "muff"
                 ]
    if word in swearList:
        return True
    else:
        return False

def getMenuOption():
    goodInput = False
    goodResponses = ["1",
                     "2",
                     "3",
                     "q"]
    while not goodInput:
        response = raw_input("Make a selection: ")
        if response.lower() in goodResponses:
            goodInput = True
        else:
            print "git gud"
    return response.lower()

def getWord(prompt):
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        if isSwear(response):
            goodInput = False
            print "Don't use that kind of language with me!"
    return response

def getEdWord(prompt):
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        if isSwear(response):
            goodInput = False
            print "Please don't swear, think of the children... Not like that you sicko!"
        if response[-2:] != "ed":
            goodInput = False
            print "Please end in ed."
    return response
        
def getIngWord(prompt):
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        if isSwear(response):
            goodInput = False
            print "Don't. Fucking. Swear."
        if response[-3:] != "ing":
            goodInput = False
            print "Please end in ing."
    return response


def getNumber(prompt):
    goodInput = False
    numbers = "0123456789."
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        for character in response:
            if character not in numbers:
                goodInput = False
                print "Numbers only please!"
    return response
        
def getColor(prompt):
    goodInput = False
    colors = " red, blue, green, yellow, orange, purple, pink, lavender,black, white"
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        for character in (response):
            if character not in colors:
                goodInput = False
                print "specified colors only"
    return response
        



















