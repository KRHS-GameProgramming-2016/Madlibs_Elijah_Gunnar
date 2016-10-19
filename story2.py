from input import*

def story(): 
    noun1 = getWord("Enter Name :")
    verb1 = getWord("Enter Activity :")
    verb2 = getWord("Enter Ability :")
    noun2 = getWord("Enter Location :")
    noun3 = getWord("Enter Name :")
    
    text = ""
    text += "once upon a time there was a child named "+noun1+"." 
    text += " this child was different from the others, "+noun1+"'s favortie activity " 
    text += "was "+verb1+". "+noun1+" eventually found out that they had a special ability,"
    text += " they found out that they had the ability to "+verb2+"."
    text += ""+noun1+" also found out that his power could be used for good or for evil."
    text += " Knowing about his special ability "+noun1+" set out to perform good deeds, he was on his way to "+noun2
    text += " when he saw "+noun3+" beating one of his friends. "+noun1+" quickly intervened using his power to "+verb2
    text += " to defeat "+noun3+" and save his freind."

    return text
