l=[12,3,4,5,6,78]
def prime(l):
    for i in l:
        for j in range(2,i):
            if i%j==0:
                print(i,"is not prime")
                break
        else:
            print(i,"is prime")
prime(l)


from functools import reduce
r=reduce(lambda x,y:x*y,l)
print(r)

l1=list(map(lambda x:x*x,l ))
print(l1)

l2=list(filter(lambda x:x%2==0,l))
print(l2)