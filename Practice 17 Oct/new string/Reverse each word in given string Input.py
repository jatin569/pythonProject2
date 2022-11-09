# Reverse each word in given string Input

s = input("Enter string : ")

s = s.split()

a = ''
for i in s:
    a = a+ i[::-1]+' '
print(a)
