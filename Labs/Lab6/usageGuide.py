import numpy as np
import matplotlib.pyplot as plt

aFigure = plt.figure() #<--- MAKES AN EMPTY FIGURE
aFigure.suptitle("No axes on this figure") #suptitle (Super title)

aFigure, ax_lst = plt.subplots(2, 2) #figure w/ 2x2 subplots grid w/ axes

#ALL plotting functions expect np.array or np.ma.masked_array
plt.show()