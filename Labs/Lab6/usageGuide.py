import numpy as np
import matplotlib.pyplot as plt

aFigure = plt.figure() #<--- MAKES AN EMPTY FIGURE
aFigure.suptitle("No axes on this figure") #suptitle (Super title)

aFigure, ax_lst = plt.subplots(2, 2) #figure w/ 2x2 subplots grid w/ axes

#ALL plotting functions expect np.array or np.ma.masked_array
plt.show()

#####################################################################################################################
x = np.linspace(0, 2, 100) #Return evenly spaced numbers over a specified interval. (start, stop, number count)
print("x is type: " + str(type(x)))

plt.plot(x, x, label="linear") #(dataset to plot on x axis, dataset to map on y axis, label for the curve)
plt.plot(x, x**2, label="quadratic")
plt.plot(x, x**3, label="cubic")

plt.xlabel("x label")
plt.ylabel("y label")

plt.title("Simple Plot")

plt.legend()

plt.show()
#####################################################################################################################
#larger step value would better approximate a function, but contains more data
x = np.arange(0, 10, 0.2) #creates an np object of values between 0-10 with step 0.2

y = np.sin(x) #creates an np object of values sin(corresponding x value)
fig, ax = plt.subplots() #uses value unpacking with tuples; assigns fig plt.subplots()[0] and ax plt.subplots()[1]
ax.plot(x, y)
plt.show()
#####################################################################################################################
def plotter(ax, x, y, param_dictionary):
    out = ax.plot(x, y, **param_dictionary) #**name allows you to pass in indefinite amount of arguments through a function
    return out

data1, data2, data3, data4 = np.random.randn(4, 100) #generates an array of random numbers 4x100
fig, (ax1, ax2) = plt.subplots(1, 2) #the subplots() methods creates both a figure AND a set of subplots
plotter(ax1, data1, data2, {"marker" : "x"}) #the "marker" kwarg sets the shape of the point
plotter(ax2, data3, data4, {"marker" : "o"})

plt.show()