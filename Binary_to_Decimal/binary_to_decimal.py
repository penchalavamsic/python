#converting binary number to decimal number
bnumber=list(input("Enter the binary number"))
value=0
for i in range(len(bnumber)):
    dec_number=bnumber.pop()
    if dec_number=='1':
        value=value+pow(2,i)
print("The decimal number is:", value)
