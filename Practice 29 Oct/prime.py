n=int(input("enter number"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not a prime number")
            break
    else:
        print("prime number")
else:
    print("invalid data")

n=int(input("enter number"))
for i in range(2,n):
    for  j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)