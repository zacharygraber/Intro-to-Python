#all of the work herein is solely mine

def alphaFunction():
    """
    INPUT nothing
    READ the file happy.txt
    RETURN a dict of lowercase letters counted
    """
    d = {}
    for i in range(97,123):
        d[chr(i)] = 0
    
    with open("Assignment6/happy.txt", "r") as f:
        contents = f.read()
        for i in contents:
            ordi = ord(i)
            if ordi > 96 and ordi < 123:
                d[i] += 1
    
    return d
                        
if __name__ == "__main__":
    returnOfTheDict = alphaFunction()
    for i in returnOfTheDict:
        print(i,returnOfTheDict[i])