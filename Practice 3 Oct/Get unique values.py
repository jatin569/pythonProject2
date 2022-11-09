l=[1,2,3,3,4,2,1]
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)