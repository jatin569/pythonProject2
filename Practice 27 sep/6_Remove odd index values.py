#Remove odd index values

str=input("Enter string: ")
str1=""
for i in range(0,len(str)):
    if i%2==0:
        str1=str1+str[i]
print(str1)