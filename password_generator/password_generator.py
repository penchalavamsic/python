import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', ':', ';', '<', '>', ',', '.', '?', '/', '|', '', '`', '~']
print("Complete the below requirments for password generation")
n_letters=int(input("How many letters should have: \n"))
n_numbers=int(input("How many numbers sholud have: \n"))
n_symbols=int(input("How many symbols should have: \n"))
password_l=[]
for i in range(1, n_letters+1):
    char=random.choice(letters)
    password_l += char
for i in range(1, n_numbers+1):
    char=random.choice(numbers)
    password_l += char
for i in range(1, n_symbols+1):
    char=random.choice(symbols)
    password_l += char
random.shuffle(password_l)
fpassword=""
for i in password_l:
    fpassword += i
print(fpassword)




