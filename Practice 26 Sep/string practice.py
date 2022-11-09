#Exercise 1B: Create a string made of the middle three characters

n=input("enter string: ")

l=len(n)
mid=int(l/2)
f=n[mid-1]
f=f+n[mid]+n[mid+1]
print(f)