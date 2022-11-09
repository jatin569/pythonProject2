#Exercise 3: Create a new string made of the first, middle, and last characters of each input string

s1=input("Enter first string: ")
s2=input("Enter second string: ")

l1=len(s1)
l2=len(s2)
a=s1[0]+s2[0]+s1[int(l1/2)]+s2[int(l2/2)]+s1[l1-1]+s2[l2-1]

print(a)