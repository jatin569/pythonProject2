#Exercise 1A: Create a string made of the first, middle and last character

n=input("Enter string: ")
l=len(n)
mid=int(l/2)
res=n[0]
res=res+n[mid]
res=res+n[l-1]
print(res)

