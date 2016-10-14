from input import *

#Written by Gunnar
def story():
    location1 = getWord("Enter a location: ")
    temperature1 = getWord("Enter a life decision: ")
    noun1 = getWord("Enter Name: ")
    noun2 = getWord("Enter Thing: ")
    noun3 = getWord("Enter An Organism: ")
    verb1 = getWord("Enter Action: ")
    verb2 = getWord("Enter Violent Action: ")
    verb3 = getWord("Enter Feeling: ")
    adjective1 = getWord("Enter Object: ")
    whatever1 = getWord("Enter Random uniteligble screeching: ")
    whatever2 = getWord("Enter Random uniteligble screeching, again: ")
    
    text = ""
    text += " Upon the hellish landscape of " + location1","
    text += noun1 + " decided that " + adjective1 + " was against their religion."
    text += " walking towards the " + adjective1 + " , " + noun1 + " encountered Elijah sitting in the " + location1
    text += " As " + noun1 + " was beginning to " + verb1
    text += " a large " + noun3 + " suddenly appeared, " + whatever1
    text += noun1 + " approached " + noun3 + " screaming loudly "
    text += whatever2 + " then suddenly " + noun3 + " turned into a large " 
    text += noun1 + " was very " + verb3 + " unable to cope with the feelings. "
    text += noun1 + " ran away from the " + verb3 + " shouting at the top of theri lungs "
    text += whatever1 

    return text
