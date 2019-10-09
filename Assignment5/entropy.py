#all of the work herein is solely mine

import math
def makeProbability(xlst):
    """
    INPUT a list of items of any type
    RETURN a list of probability of those items, in order of appearance
    """
    items = {}
    returnList = []
    for i in xlst: #iterate over original list, using a dict for search
        if not i in items:
            items[i] = 1 #if the item (key) not already in items dict, then add it
        else:
            items[i] += 1 #else increment the frequency (value)
    for i in items:
        returnList += [items[i] / len(xlst)] #grab values in items dict, and turn them into a list of probabilities
    return returnList

def entropy(xlst):
    """
    INPUT a list of probabilities
    RETURN a float entropy
    """
    currentSum = 0
    for i in xlst:
        currentSum += (i * math.log2(i))
    if currentSum:
        return -1 * currentSum
    return 0.0

if __name__ == "__main__":
    s1 = ["a","b","a","b","a","b","b","b"]
    s2 = [(1),(2),(3),(4)]
    s3 = [1]
    s4 = [1,2]
    xlst = [s1,s2,s3,s4]
    for i in xlst:
        print(makeProbability(i))
        print(entropy(makeProbability(i)))