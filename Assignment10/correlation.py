import matplotlib.pyplot as plt
import numpy as np

def mean(lst):
    # TODO: Implement function
	return 1

def sd(xlst):
    # TODO: Implement function
    return 1

def r(x, y):
    # TODO: Implement function
    return 1

def theGraph():
    pass
    # TODO: Implement function (D2)


if __name__ == "__main__":
    x = [[2,3],[4,3],[1,1.4],[1,.5],[5,3]]

    # TODO: Complete code (D1) by calling the important function

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