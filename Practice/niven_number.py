number=18
sum=0
while(number!=0):
    n=number%10
    sum=sum+n
    number=number//10
print(sum)
div=number%sum
if(div==0):
    print("Niven Number")
else:
    print("Not niven number")
