a={'a':5,'b':3,'d':4,'c':1}
# out={'c':1,'b':3,'d':4,'a':5}

val=list(a.values())
print(val)
for i in range(len(val)):
    for j in range(i+1,len(val)):
        if val[i] >val[j]:
            val[i], val[j] = val[j], val[i]
print(val)

dict1={}

for i in range(len(val)):
    for j in a:
        if val[i] == a[j]:
            dict1[j] = val[i]

print(dict1)