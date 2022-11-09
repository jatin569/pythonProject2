n=int(input("enter number: "))
for i in range(1,n):
    n=n*i
print(n)



def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter number: "))
print(fact(n))