#Exercise 2: Append new string in the middle of a given string

s1=input("Enter string: ")
s2=input("Enter string: ")

s3=" "
l=len(s1)
mid=int(l/2)
x=s1[:mid]
x=x+s2
x=x+s1[mid:]
print(x)