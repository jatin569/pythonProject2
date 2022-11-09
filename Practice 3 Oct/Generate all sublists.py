def sublist(l):
    l1=[()]
    for i in range(len(l)):
        for j in range(i):
            l1.append(l[j:i+1])
    return l1
l=[1,2,3,4,5]
print(sublist(l))