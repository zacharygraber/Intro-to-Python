import random, string

#######GENERATOR
def randomValues(maxInt, length):
    """
    An Iterator that produces random values
    """
    i = 0
    while i < length:
        yield random.randint(0,maxInt)
        i += 1

#########COMPREHENSIONS
def dictionary1(letters):
    """
    Given a string of letters, set up a blank counter
    """
    return {L:0 for L in letters}

def dictionary2(flip):
    """
    Assuming all unique values, flip the dict keys and values
    """
    return {flip[k]: k for k in flip}

def onlyStrings(listOfKeys):
    """
    Provides a counting dict that only has keys of strings
    """
    return {k:0 for k in listOfKeys if type(k) == str}

############LIST COMPREHENSION
def matrix(rows, columns, defaultValue):
    """
    Create a matrix with that number of rows and columns

    Default value is value for each spot
    """
    return [[defaultValue for c in range(columns)] for r in range(rows)]

def evens(maximum):
    """
    Create a list of evens from 0 to max number (exclusive)
    """
    return [i for i in range(maximum) if i % 2 == 0]

if __name__ == "__main__":
    ##########GENERATOR
    g = randomValues(10,10)
    print("Generator:", [x for x in g])
    ##########Dict Comprehension
    print()
    print("Dictionary Comprehension:",dictionary1(string.ascii_lowercase))
    print("Dictionary Comprehension:",dictionary1("SICE"))
    temp = {s:i for s,i in zip(string.hexdigits,range(0,16))}
    print("Dictionary Comprehension:",dictionary2(temp))
    values = ["1",1,"2",2,3,"3"]
    print("Dictionary Comprehension:",onlyStrings(values))
    ##########List Comprehension
    print()
    print("List Comprehension:",matrix(4,5,"a"))
    print("List Comprehension:",matrix(5,1,0))
    print("List Comprehension:",evens(10))