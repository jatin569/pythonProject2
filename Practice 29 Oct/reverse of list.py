l=[1,2,3,4,567]
l2=[]
for i in range(len(l)-1,-1,-1):
    l2.append(l[i])
print(l2)

l1=['a','b','c','a','b','d']
d={}
for i in l1:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)