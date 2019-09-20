def sumListFor(aList):
    """
    Sums all numbers in a list using a for-loop.
    Returns the sum of all numbers.
    """
    result = 0
    for number in aList:
        result += number
    return result

def neverGonna(listOfWrongDoings):
    """
    Print out "never gonna " + doSomething
    """
    for doing in listOfWrongDoings:
        print("Never gonna " + doing)