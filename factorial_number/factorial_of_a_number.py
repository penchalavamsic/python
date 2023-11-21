n=int(input("enter the number"))
factorial=1
if(n>=1):
    for i in range(1,n+1):
        factorial=factorial*i
    print(factorial)


#using math module and factorial function
import math
num=int(input("Enter the number"))
factorial=math.factorial(num)
print("The factorial of", num,"is",factorial)