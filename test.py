import string
import numpy as np
d=[['1','2'],['3','4']]
with open('stardata.csv','r') as f:    #creating a list with lines of file as elements
    lines=f.read().split('\n')
data_stars=[]   #splitting the lines according to commas, now you have a nested list with planet, moon, diameter
for line in lines:
    data_stars.append(line.split(','))
arr=np.array(data_stars, dtype=object)
print(arr)
print(arr.shape)