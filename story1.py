from input import *

#Written by Gunnar
def story():
    location1 = getWord("Enter a location: ")
    temperature1 = getWord("Enter a life decision: ")
    noun1 = getWord("Enter Name: ")
    noun2 = getWord("Enter Thing: ")
    noun4 = getWord("Enter Another Thing: ")
    noun3 = getWord("Enter An Organism: ")
    verb1 = getWord("Enter Action: ")
    verb2 = getWord("Enter Violent Action: ")
    verb3 = getWord("Enter Feeling: ")
    adjective1 = getWord("Enter Object: ")
    whatever1 = getWord("Enter Random uniteligble screeching: ")
    whatever2 = getWord("Enter Random uniteligble screeching, again: ")
    
    text = ""
    text += "Upon the hellish landscape of " + location1 + ", "
    text += noun1 + " the destoryer of worlds, stumbled upon a small" + adjective1 + "." 
    text += " Walking towards the " + adjective1 + ", " + noun1
    text += " was deciding on how they would deal with the " + adjective1 + ". "
    text += verb2 + " " + noun1 + " decided to themselves, that should " + verb1
    text += " that  " + noun3 + " suddenly appeared, " + whatever1
    text += noun1 + " approached " + noun3 + " screaming loudly "
    text += whatever2 + " then suddenly " + noun3 + " turned into a large " + noun4 + " ! "
    text += noun1 + " was very " + verb3 + " . As they are unable to cope with the feelings. "
    text += noun1 + " ran away from the " + verb3 + " shouting at the top of theri lungs "
    text += whatever1 

    return text
