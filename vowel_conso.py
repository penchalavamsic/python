a=input()
b="aeiouAEIOU"
if a in b:
    print("vowel")
else:
    print("consonants")

c=0
for i in a:
    if i in b:
        c+=1
print(c)