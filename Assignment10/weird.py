import matplotlib.pyplot as plt

### TODO: Answer question in the comments here
# The graph shown models the value of n with respect to the recursion depth i
# I am struggling to find patterns in differing values of n, except that odd values tend to give more peaks and valleys
#    also, each pair of outputs (starting at every other) is a number and its half
# Calling g(n,i) with different starting i values seems to have no effect on the graph

xlst, ylst = [],[]

def f(n):
    if not n % 2:
        return n // 2
    else:
        return (3*n) + 1

def g(n,i):
    xlst.append(i)
    ylst.append(n)

    print(str(n)+" ",end="")
    if n == 1:
        return 1
    else:
        return g(f(n), i+1)

if __name__ == "__main__":
    g(26,0)
    xmax = max(tuple(xlst))
    ymax = max(tuple(ylst))
    print("\nNumber of recursive calls: {0}\nMaximum number: {1}".format(xmax,ymax))
    plt.plot(xlst,ylst,'r--')
    plt.axis([0,xmax,0,ymax])
    plt.show()