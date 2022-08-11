# import all the important packages

import numpy as np
from scipy.optimize import curve_fit as cf
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,2,3,4,5]
z=[6,7,8,9,10]
a=[6,7,8,9,10]
fig, ax=plt.subplots(1,2)

ax[0].plot(x,y)
ax[1].plot(z,a)
plt.show()
