l = [1,5,6,3,9]
print(min(l))
s=l[0]
for i in l:
    if i<s:
        s=i
print(s)