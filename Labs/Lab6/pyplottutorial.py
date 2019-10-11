import numpy as np
import matplotlib.pyplot as plt

plt.plot([1,2,3,7]) #a single list is assumed to be a set of y values
plt.ylabel("some numbers")
plt.show()

plt.plot([1,2,3,4],[1,5,8,3], "b-") #"b-" represents a solid blue line
plt.plot([1,2,3,4],[1,5,8,3], "ro") #"ro" is red circles
plt.axis([0,6,0,20]) #controls range of axes
plt.show()

#NOTE plt.plot() can take lists, but always will yield a numpy array

#NOTE if you have data in a dict, then you can use the data keyword
myData = {"a": np.arange(50),
          "c": np.random.randint(0,50,50),
          "d": np.random.randn(50)}

myData["b"] = myData["a"] + 10 * np.random.randn(50)
myData["d"] = np.abs(myData["d"]) * 100

plt.scatter("a", "b", c="c", s="d", data=myData) #creates a scatterplot with data in myData dict
plt.text(20, 40, "hi!")
plt.show()

