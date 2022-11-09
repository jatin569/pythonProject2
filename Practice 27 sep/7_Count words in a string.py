#Count words in a string

str=input("Enter string: ")
count=0
for i in str:
    if i.isalpha():
        count+=1
print("no of words: ",count)