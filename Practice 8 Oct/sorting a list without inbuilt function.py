a=[1,4,3,2,8,5]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
            print(a)
print(a)