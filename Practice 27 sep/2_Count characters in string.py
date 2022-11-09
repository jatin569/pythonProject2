#Count characters in string

str=input("Enter string: ")
c=0
for i in str:
    if i.isalpha():
        c+=1
print(c)
s=str.count("a")
print(s)



print("................end.................")