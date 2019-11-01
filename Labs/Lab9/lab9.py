import random

### Generators

def diceRolls(diceList):
    """
    Given a list of tuples, where each tuple is structured as:

    (size of dice, number of rolls)

    Where the "size of the dice" is rolled that many times in a row. 
    Each call to the generator produces a single value. 
    You will need to use a certain function from the 
    `random` module. 

    ---------------------------------------------------------------------------
    Example:
    >>> tuples = [(20, 4), (6, 3)]
    >>> print([i for i in diceRolls(tuples)])
    [13, 17, 18, 17, 5, 6, 1] 
    # Note that this will be a different list because of random
    """
    for i in diceList:
        count = 0
        while count < i[1]:
            yield random.randint(1,i[0])
            count += 1



### List Comprehension

"""
All list comprehensions must be written as one expression. 

While coding them, it is alright to test with multiple lines, 
but when finalizing your solution for a problem, condense it 
into one expression.
"""

def splitCharacters(word):
    """
    Given a single word, split up each character into it's own element within a list. 

    Extra challenge, you cannot keep spaces (' ' (ignore quotes)).
    """
    return [i for i in word if i != " "]

def oddNumbers():
    """
    Return a list of all odd numbers less than 50
    """
    return [i for i in range(1,50,2)]

def dictionaryProblem(d):
    """
    Given a dictionary, where each key is a string and a value is a number, 
    create a dictionary with all keys and their associated value that have a 
    value over 1
    """
    return {i: d[i] for i in d if d[i] > 1}

### Memoized

memoDict = {0:0,1:1}
def fibMemo(n):
    """
    Given the nth fibonacci number, calculate the value. 

    Do this with memoization (determine where to put the dictionary)

    Fib(0) = 0
    Fib(1) = 1
    Fib(2) = 1
    Fib(3) = 3
    ...
    Fib(11) = 89
    """
    if n in memoDict:
        return memoDict[n]
    else:
        memoDict[n] = fibMemo(n-1) + fibMemo(n-2)
        return memoDict[n]

### Test code

if __name__ == "__main__":
    tuples = [(20, 4), (6, 3)]
    print("Dice Rolls:",[i for i in diceRolls(tuples)])
    print("FibMemo:",fibMemo(11))