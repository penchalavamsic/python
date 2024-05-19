import numpy as b
a=b.array([[12,5,8,0],[5,9,0,1]])
print(a)
print(a[a>10])
c=b.nonzero(a>10) #returns non zero indexs as tuples
print(c)