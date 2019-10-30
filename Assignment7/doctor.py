def doctor():
    count = 0
    symTup = ("abdominal pain","nausea","vomiting","fever","loss of appetite")
    for i in symTup:
        if count > 2:
            return "Appendicitis"
        validInput = False
        while not validInput:
            try:
                count += int(input("Do you have {0}: 1/0 ".format(i)))
                validInput = True
            except ValueError:
                validInput = False
    return "No Appendicitis"
        
print(doctor())