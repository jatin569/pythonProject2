#takes a list and returns a new list with unique elements of the first list.

def unique(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1
l=[3,5,7,7,45,4,2,7,1,8]
print(unique(l))






