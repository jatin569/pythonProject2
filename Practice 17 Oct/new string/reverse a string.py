# reverse a string

str1 = input("Enter String : ")

str2=''

for i in range(len(str1)):
    str2=str2+str1[-i-1]
print(str2)

