# compute sum of digits of a given string

s = input("Enter string : ")
sum = 0
for i in s:
    if i.isdigit():
        sum=sum+int(i)
print(sum)