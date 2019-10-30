# import random #for testing

def min(x,y):
    if x < y:
        return x
    return y

def MIN(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return min(lst[0],MIN(lst[1:]))

def min1(x):
    """
    Finds the minimum of a list using a for-loop and indices
    """
    if not x:
        return None
    smallest = x[0]
    for i in range(1,len(x)):
        if x[i] < smallest:
            smallest = x[i]
    return smallest

def min2(x):
    """
    Finds the minimum of a list using a for loop and container
    """
    if not x:
        return None
    smallest = x[0]
    for i in x:
        if i < smallest:
            smallest = i
    return smallest

def min3(x):
    """
    Finds the minimum of a list using a while-loop and indices
    """
    if not x:
        return None
    smallest = x[0]
    i = 1
    while i < len(x):
        if x[i] < smallest:
            smallest = x[i]
        i += 1
    return smallest

def min4(x):
    """
    Finds the minimum of a list using a while-loop and a container
    """
    if not x:
        return None
    xCopy = x
    smallest = x[0]
    while xCopy:
        if xCopy[0] < smallest:
            smallest = xCopy[0]
        xCopy = xCopy[1:]
    return smallest

def min5(x):
    small = x[-1]
    for i in range(len(x)-1,-1,-1):
        if x[i] < small:
            small = x[i]
    return small

if __name__ == "__main__":
    
    #Testing MIN######################################################
    # for i in range(10):
    #     test = [random.randint(1,100) for i in range(10)]
    #     print(test,"MIN ----> ",MIN(test))
    #     print(test,"min1 ----> ",min1(test))
    #     print(test,"min2 ----> ",min2(test))
    #     print(test,"min3 ----> ",min3(test))
    #     print(test,"min4 ----> ",min4(test))
    ##################################################################

    x = [1,42,-1,22,0,12]

    mf = [MIN, min1, min2, min3, min4, min5]

    for f in mf:
        print("{0}({1}) = {2}".format(f.__name__,x,f(x)))