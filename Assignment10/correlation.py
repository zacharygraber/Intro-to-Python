import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

def mean(lst):
	return sum(lst) / len(lst)

def sd(xlst):
    sigma = []
    xlstMean = mean(xlst)
    for xi in xlst:
        sigma += [(xi - xlstMean)**2]
    return sqrt(( 1 / (len(xlst) - 1)) * sum(sigma))

def r(x, y):
    #print(sd(x))
    sigma = []
    xMean = mean(x)
    yMean = mean(y)
    for i in range(len(x)):
        sigma += [((x[i] - xMean) / (sd(x))) * ((y[i] - yMean) / (sd(y)))]
    return (1/(len(x)-1)) * sum(sigma)

def theGraph():
    def leastSquareBestFit(x,y):
        xMean = mean(x)
        yMean = mean(y)
        numSigma = [(x[i] - xMean) * (y[i] - yMean) for i in range(len(x))]
        denSigma = [(x[i] - xMean)**2 for i in range(len(x))]

        slope = sum(numSigma) / sum(denSigma)
        intercept = yMean - (slope * xMean)
        return lambda x: (slope*x) + intercept

    # open the file and generate a list dat with the coordinates listed as space-separated strings
    with open("Assignment10/acme_zyx.txt") as f:
        dat = (f.read()).splitlines()
    
    # convert each coordinate into a list of strings
    for i in range(len(dat)):
        dat[i] = dat[i].split()
    
    # generate lists of float x and y values
    x = [float(i[0]) for i in dat]
    y = [float(i[1]) for i in dat]
    abscissa = np.arange(0,125,5)
    
    rValue = r(x,y)
    plt.plot(x,y, "ro")
    plt.plot(abscissa,leastSquareBestFit(x,y)(abscissa), "g--")
    
    plt.axis([0,120,0,210])
    plt.xlabel("ACME")
    plt.ylabel("ZYX")
    plt.title("r = {0:0.3}".format(rValue))
    plt.savefig(fname="Assignment10/stock.png")




if __name__ == "__main__":
    x = [[2,3],[4,3],[1,1.4],[1,.5],[5,3]]

    # Complete code (D1) by calling the important function
    rValue = r([i[0] for i in x],[i[1] for i in x])

    print(rValue)
    # Example of creating a plot
    plt.plot([i[0] for i in x],[i[1] for i in x], 'ro')
    t = np.arange(0,6,.1)
    plt.plot(t,t*.65 + .5,'g--')
    plt.axis([0,6,0,6])
    plt.xlabel("A values")
    plt.ylabel("B value")
    plt.title("r = {0:.3}".format(rValue))
    plt.show()

    theGraph()