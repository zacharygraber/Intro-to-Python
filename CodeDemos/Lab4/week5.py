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