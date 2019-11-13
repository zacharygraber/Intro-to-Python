#At any given point in time, the chance of taking a step in each direction is essentially
#25 percent, meaning that the 'person' is equally as likely to step back toward the starting
#point, as he is to step away from it, meaning that little progress is ever made.
#What results from this is usually movement that ends with little displacement, since equal
#amounts of progress and setback occur.

#As such, one must surpass a large number (about 1,000) of steps before he or she ends up
#even 30 steps away from the center, measured diagonally.

import numpy as np
import matplotlib.pyplot as plt
import random as rn


#translates a random int into a step along the random walk
#parameters: int i for the step index, numpy array x for tracking the left/right location at index i,
#numpy array y for tracking the forward/backward location at index i
#return: none
def step(x,y,i):
    direction = rn.randint(1,4)
    if direction == 1:
        x[i] = x[i-1] + 1
        y[i] = y[i-1]
    elif direction == 2:
        x[i] = x[i-1] - 1
        y[i] = y[i-1]
    elif direction == 3:
        x[i] = x[i-1]
        y[i] = y[i-1] + 1
    else:
        x[i] = x[i-1]
        y[i] = y[i-1] - 1

def graphit(x,y,n):
    plt.title("Random {0} Walk\nLast Location {1},{2}".format(n,int(x[n-1]),int(y[n-1])) )
    plt.plot(x,y) 
    plt.plot([x[1],x[1]],[y[1]-10,y[1]+10], "b-")
    plt.plot([x[1]-10,x[1]+10],[y[1],y[1]], "b-")
    plt.plot([x[n-1]-10,x[n-1]+10],[y[n-1],y[n-1]], "r-")
    plt.plot([x[n-1],x[n-1]],[y[n-1]-10,y[n-1]+10], "r-")
    plt.savefig("rand_walk"+str(n)+".png",bbox_inches="tight",dpi=600) 
    plt.show() 


n = int(input("Number of steps: "))

x = np.zeros(n) 
y = np.zeros(n) 

for i in range(1,n):
    step(x,y,i)

graphit(x,y,n)