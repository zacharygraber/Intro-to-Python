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
