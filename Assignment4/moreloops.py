#All of the work herein is solely mine

# Input Parameter: a list of, possibly empty, numbers x
# Returns: the max number in list x (does not have to be unique)
def maxFor(xlst):
    """
    Uses a for loop to determine the maximum value in a list of numbers (can be empty)
    Returns a number (int or float) literal, not an index
    """
    if not xlst:
        return None
    
    maxValue = xlst[0]
    for i in range(len(xlst)):
        if xlst[i] > maxValue:
            maxValue = xlst[i]
    return maxValue
 
# Input Parameter: a list of, possibly empty, numbers x
# Returns: the max number in list x (does not have to be unique)
def maxWhile(xlst):
    """
    Uses a while loop to determine the maximum value in a list of numbers (can be empty)
    Returns a number (int or float) literal, not an index
    """
    if not xlst:
        return None
    
    maxValue = xlst[0]
    i = 0
    while i < len(xlst):
        if xlst[i] > maxValue:
            maxValue = xlst[i]
        i += 1
    return maxValue

def minFor(xlst):
    """
    Input: a non-empty list of numbers x
    Returns: the minimal number value in list x (does not have to be unique)
    """
    if not xlst:
        return None
    
    minValue = xlst[0]
    for i in range(len(xlst)):
        if xlst[i] < minValue:
            minValue = xlst[i]
    return minValue

def RemoveEvens(xlst):
    """
    Input Parameters:a list of numbers lst
    Returns: the list lst with all occurrences of evens removed
    """
    newList = list()
    for i in xlst:
        if i % 2:
            newList += [i]
    return newList
#TODO: implement this function using for

def myReplace(oldX, num, newX, xlst):
    """
    Input Parameters: list that contains either integers or strings
    Return Value: oldX replaced with num copies of newX
    """
    newList = list()
    for i in xlst:
        if i == oldX:
            newList += [newX] * num
        else:
            newList += [i]
    return newList

def sumOdd(xlst):
    """
    Input Parameters: list of numbers
    Returns: sum of the odd numbers
    if there are no odd numbers, then print zero
    if the list is empty, print the empty list
    """
    if not xlst:
        return xlst
        #print("The List ({0}) is Empty".format(xlst))

    currentSum = 0
    i = 0
    while i < len(xlst):
        if xlst[i] % 2:
            currentSum += xlst[i]
        i += 1
    return currentSum

def StringConcat(xlst):
    """
    Input Parameter: a list x of objects [x1, x2, x3,..., xn]
    Returns: a string that is the concatenation of all the strings
    in the list in order encountered
    """
    returnString = str()
    for i in xlst:
        if type(i) == str:
            returnString += i
    return returnString
#TODO: implement this function

# Data
w = []
x = [1,42,24,22,61,100,0,42]
y = [2]
z = [555,333,222]
nlst = [w,x,y,z]
c = [0,1,1,0,2,1,4]
a = ["a","b","b", "a", "c","b","e"]
b = [1,1,2,1,1,2,1,1,2,1,3,1]
d = ["a",1,"row",0,3,"d","ef",453]

if __name__ == "__main__":
    print("maxFor_____")
    for i in nlst:
        print(maxFor(i))
    print("\nmaxWhile_____")
    for i in nlst:
        print(maxWhile(i))
    print("\nminFor_____")
    for i in nlst:
        print(minFor(i))
    print("\nRemoveEvens_____")
    print(RemoveEvens(b))
    print(RemoveEvens(c))
    print("\nmyReplace_____")
    print(myReplace(1,2,"dog",c))
    print(myReplace(1,2,1,b))
    print("\nsumOdd_____")
    for i in nlst:
        print(sumOdd(i))
    print("\nStringConcat_____")
    print(StringConcat(a))
    print(StringConcat(d))