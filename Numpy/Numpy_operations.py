#numpy pad method 
import numpy as np
a1=np.full((4,4),5) # creates array with full of 5 number
a2 = np.pad(a1, pad_width=2, mode='constant',constant_values=1)
print(a2)

b1=np.ones((2,2)) #creates 2*2 of 1 values of array
b2=np.pad(b1,pad_width=1, mode='minimum')
print(b2)
