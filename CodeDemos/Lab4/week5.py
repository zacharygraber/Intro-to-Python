def occurencesWhile(lst, var):
    """
    Using a while loop, find the number of occurences in the list
    """
    #returns int representing number of occurences
    occurNo = 0

    i = 0 #index variable
    while i < len(lst): #iterate once for every item in lst
        if lst[i] == var:
            occurNo += 1 #count an occurence if the item is the var
        i += 1 #increment the index
    return occurNo

def occurencesWhileList(lst, var):
    """
    Using a while loop, find the numbe rof occurences in the list

    The exception is: you must use lst as the condition
    """
    item = 0
    while lst: #while there are item(s) in the list
        if lst[0] == var:
            item += 1
        lst = lst[1:] #remove the first item in the list
    return item

def operationList(opsList, op):
    """
    Given a list of lists, where each inner list has a size > 0

    Using the operation provide:
    -subtract: s
    -multiply: m
    -add: a

    Apply that to the whole list
    """
    resultingList = []
    index1 = 0
    while index1 < len(opsList):
        currList = opsList[index1]
        if op == "m":
            currResult = 1
        else:
            currResult = 0
        index2 = 0
        while index2 < len(currList):
            if op == "m":
                currResult *= currList[index2]
            elif op == "a":
                currResult += currList[index2]
            else:
                currResult -= currList[index2]
            index2 += 1
        index1 += 1
        resultingList += [currResult]
    return resultingList

def evenCount2(dictionary):
    count = 0
    for key in dictionary: #for key in dictionary.keys()
        if key % 2 ==0:
            count += 1
    return count