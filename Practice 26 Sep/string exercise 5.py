#Exercise 4: Arrange string characters such that lowercase letters should come first
n=input("enter string: ")
n1=""
n2=""

for i in n:
    if i.islower():
        n1=n1+i
    else:
        n2=n2+i
sorted_str = n1 + n2
print('Result:', sorted_str)

