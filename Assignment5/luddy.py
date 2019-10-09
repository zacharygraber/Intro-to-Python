#all of the work herein is solely mine

import numpy as np

def area(x: int or float,y: int or float):
    """
    INPUT dimensions x and y in feet
    RETURN boolean whether or not the area is 75 feet**2
    """
    return x * y == 75

def f(x,y):
    """
    INPUT dimensions x and y
    RETURN minimal price in USD
    """
    if x > y:
        return y*20 + x*10 + x*5
    else:
        return x*20 + y*10 + y*5

#MARVELOUS BRUTE FORCE
length = np.arange(0,100,0.25)
height = np.arange(0,100,0.25)

ax = length[-1] #start with largest possible values
by = height[-1]
currLow = f(ax,by)
for i in length: #NOTE there will be repeat pairings, but they yield the same price
    for j in height:
        if area(i,j) and f(i,j) < currLow:
            ax = i
            by = j
            currLow = f(i,j)

if __name__ == "__main__":
    print(ax,by, f(ax,by))