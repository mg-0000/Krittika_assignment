# import all the important packages

import numpy as np
from scipy.optimize import curve_fit as cf
import matplotlib.pyplot as plt

# Step 1: Define your model as a callable function with the first argument as observation points/inputs and
#         consequent arguments as the parameters of your model. The output of this function should be your
#         model's predictions

def lin_func(x,m,c):
    return m*x + c

with open('data.txt','r') as f2:    #creating a list with lines of file as elements
    lines2=f2.read().split('\n')
data_uni=[]   #splitting the lines according to commas, now you have a nested list with planet, moon, diameter
for line in lines2:
    data_uni.append(line.split(','))
del data_uni[0]
universe_data=np.array(data_uni)
for i in range(0,universe_data.shape[0]-1):
    universe_data[i][1]=float(universe_data[i][1])
    universe_data[i][0]=10**((float(universe_data[i][0])/5)-5)

y_data=np.zeros([universe_data.shape[0]-1,1], dtype=float)
x_data=np.zeros([universe_data.shape[0]-1,1],dtype=float)
for i in range(0,universe_data.shape[0]-1):
    y_data[i]=float(universe_data[i][0])
    x_data[i] = float(universe_data[i][1])


ydata=y_data[:,0]
xdata=x_data[:,0]



#plt.scatter(xdata,ydata,s=1)

p_opt, p_cov = cf(lin_func,xdata,ydata)


plt.plot(xdata,lin_func(xdata,*p_opt),label='Best Fit',color='g')
# * before a separable object unpacks it. So you don't need to write lin_func(xdata,p_opt[0],p_opt[1]). The *
# does it for you.
plt.scatter(xdata,ydata,label='OG_Data',s=1,color='darkorange')
# Yes, you can have scatter plot and a normal plot in one
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Fit')
plt.legend()
plt.show()