def doctor():
    count = 0
    symTup = ("abdominal pain","nausea","vomiting","fever","loss of appetite")

    #iterate through each symptom
    for i in symTup:
        if count > 2:
            return "Appendicitis" #returns from the func immediately if 3 are met

        #gets user input, making sure it's an int
        #then adds 1 to count if true and nothing if false
        validInput = bool()
        while not validInput:
            try:
                count += bool(int(input("Do you have {0}: 1/0 ".format(i)))) #bool makes sure only 1 can be added for each symptom
                validInput = True #Flag that a proper input is given, breaking the loop
            except ValueError:
                validInput = False
    return "No Appendicitis" #If all else fails...
        
print(doctor())