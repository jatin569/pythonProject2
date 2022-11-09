#reverse a tuple.
l=[]
tup=(4,2,6,1,7,8,9)
for i in range(len(tup)-1,-1,-1):
    l.append(tup[i])
l=tuple(l)
print(l)