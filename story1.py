from input import *

#Written by Gunnar
def story():
    location1 = getWord("Enter a location: ")
    temperature1 = getWord("Enter a life decision: ")
    noun1 = getWord("Enter Name: ")
    noun6 = getWord("Enter  Another Name: ")
    noun2 = getWord("Enter Thing: ")
    noun4 = getWord("Enter Another Thing: ")
    noun3 = getWord("Enter A Creature: ")
    noun5 = getColor("Enter A Color: ")
    verb1 = getWord("Enter Verb, any will do: ")
    verb2 = getWord("Enter Violent Action: ")
    verb6 = getEdWord('Enter Violent Action that ends in "d": ')
    verb3 = getWord("Enter Feeling: ")
    verb4 = getIngWord('Enter Movement that ends in "-ing": ')
    verb5 = getWord("Enter Interaction: ")
    adjective1 = getWord("Enter Object: ")
    adjective2 = getWord("Enter Intensity: ")
    adjective3 = getWord("Enter Higher Intensity: ")
    whatever1 = getWord("Enter Random uniteligble screeching: ")
    whatever2 = getWord("Enter Random uniteligble screeching, but even more uninteligble this time: ")
    
    text = ""
    text += "Upon the hellish landscape of " + location1 + ", "
    text += noun1 + ", the destoryer of worlds, stumbled upon a small " + adjective1 + "." 
    text += " Walking towards the " + adjective1 + ", " + noun1
    text += " was deciding on how they would deal with the " + adjective1 + ". "
    text += '"' + verb2 + '," ' + noun1 + ' decided to themselves, "that should ' + verb1
    text += " that little " + adjective1 + '".' + verb4 + " towards the " + adjective1 + ", "
    text += " " + noun1 + " " + adjective2 + " " + verb5 + " the " + adjective1 + ", "
    text += noun1 + " " + verb6 + " the helpless " + adjective1 + "."
    text += " Suddenly  " + adjective1 + " glowed a bright " + noun5 + ", blinding " + noun1 + "."
    text += " Opening their eyes, the destroyer of worlds was baffled by the transformation the small " + adjective1
    text += " had undergone, turning them into a " + noun3 + "! "
    text += noun1 + " felt very " + verb3 + " about the sudden transformation. Unsure how to approach the situation, "
    text += noun1 + " was not prepared for the sudden onslaught by the " + noun3 + "."
    text += '"' + whatever1 + '"' + "the destroyer of worlds was unable to stop the " + noun3 + " leaving them victim to its will."
    text += "Being " + adjective3 + " ripped apart, " + noun1 + " screamed his last as his power was transfered to the " + noun3 
    text += "." + ' "' + whatever2 + '" ' + noun6 + " the newly crowned destroyer of worlds stood above the pile of ash where "
    text += noun1 + " once stood."
    

    return text
