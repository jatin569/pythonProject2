#Last part of string

str=input("Enter string: ")
str1=""
for i in range(len(str)-1,-1,-1):
    str1=str1+str[i]
    if str[i]==" ":
        break

str1=str1[::-1]
print(str1)

#other method
li=str.split()
print(li[-1])