from input import *

#Written by Gunnar and Elijah
def story():
    location1 = getWord("Enter a location: ")
    noun1 = getWord("Enter Name: ")
    verb1 = getEdWord("Enter Action ending in -ed: ")
    adjective1 = getWord("Enter Object: ")
    noun2 = getWord("Enter Weapon: ")
    noun3 = getWord("Enter Obstacle: ")
    whatever1 = getWord("Enter Yelling Noises: ")
    
    text = ""
    text += "Among the multitude of dead bodies, " + noun1 + " was slowly crawling their way out of the pit. "
    text += "Their body covered in wounds, still, they managed to escape from " + location1 + ", where their allies lay dead and "
    text += "rotting. Standing above the mass grave, " + noun1 + " looked at those who were once friends and " + verb1
    text += " their fallen comrades. Returning to the front lines was " + noun1 + "'s only concern, leaviing their grief behind "
    text += "like the bodies that had become family to them. Picking up their " + noun2 + ", " + noun1 + " began their journey "
    text += " back into the fray. Crossing multiple " + noun3 + "s, they finally saw the warscape once again. Lifting their " 
    text += noun2 + ", " + noun1 + " yelled a battle cry: " + ' "' + whatever1 + '"' + " and launched themselves back into the fray."
    text += " Cutting down enemies left and right, vengence in their eyes, " + noun1 + " slowly pushied back the enemy until none "
    text += "were left. Finally, with the battle won, and the war far from done, " + noun1 + " grieved for those they lost."
    
    return text
