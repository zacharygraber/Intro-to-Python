import numpy as np
import matplotlib.pyplot as plt

#Simple plot
xData = np.arange(0,6.4,0.2)
yData = np.sin(xData)
plt.plot(xData, yData)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Sine")
plt.show()

#two in one window
def plotter(ax, data1, data2, **others):
    out = ax.plot(data1, data2, **others)
    return out

fig, (a1, a2) = plt.subplots(2,1)
plotter(a1, [1,2,3,4,5], [6,3,7,2,8])
plotter(a2, [5,3,7,2,5], [1,2,3,4,6])
plt.show()