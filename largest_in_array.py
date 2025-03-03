a=[10,2,5,22,0]
b=a[0]
for i in range(len(a)):
    if a[i]>b:
        b=a[i]
        print(b)