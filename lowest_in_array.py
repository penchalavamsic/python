a=list(map(int, input().split()))
b=min(a)
print(b)
c=a[0]
for i in range(len(a)):
    if a[i]<c:
        c=a[i]
        print(c)

