# reverse words in a string

str1 = input("Enter String : ")
str1 = str1.split(' ')

for i in range(len(str1)-1,-1,-1):
    print(str1[i],end=" ")