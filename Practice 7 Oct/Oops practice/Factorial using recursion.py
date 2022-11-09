def fact(n):
    if n==1:
        return 1
    else:
        return n *(fact(n-1))
print(fact(5))

#other method
n=5
fac=1
for i in range(1,n+1):
    fac=fac*i
print(fac)

#other method using lambda
a=lambda x: x == 1 or x * a(x-1)
print(a(5))