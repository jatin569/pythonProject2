# lowercase first n characters in a string

str1 = input("Enter string : ")
n=int(input("How many charcters: "))
for i in range(n):
    print(str1[i].lower(),end='')

