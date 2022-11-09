def frequency(l):
    for i in l:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    return d
d={}
print(frequency(l=[1,2,3,1,2,4,5,4,3,1]))