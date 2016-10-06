from input import *

#Written by Mr. Spooner
def story():
    location1 = getWord("Enter a location: ")
    temperature1 = getNumber("Enter a Number: ")
    noun1 = getWord("Enter Noun: ")
    noun2 = getWord("Enter Noun: ")
    
    text = ""
    text += "One day I went to the " + location1
    text += ". It was like a " + temperature1
    text += " out."
    text += " I saw a " + noun1 
    text += " walking towards " + noun2 
    text += " . " 
    return text
