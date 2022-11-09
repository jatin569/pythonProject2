l=[5,3,6,2,8,1]
a=0
l1=[]
for i in range(len(l)):
    a=min(l)
    print(a)
    l1.append(a)
    l.remove(a)

print(l1)