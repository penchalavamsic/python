import math
a=int(input())
b=int(input())
constant=int(input())
d=0
d= b*b-(4*a*constant)
if d<0:
    print("no real values")
else:
    e=(-b+math.sqrt(d))//2*a
    print(e)