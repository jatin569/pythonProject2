# Reverse each word and reverse word again. Input

s = input("Enter string : ")

s = s.split()

a = ''
b = ''
for i in s:
    a = a+ i[::-1]+' '
    b = b+ i+' '

print(a,b)

