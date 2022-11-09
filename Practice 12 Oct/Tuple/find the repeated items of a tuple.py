# find the repeated items of a tuple
l=[]
tup1 = (6, 4, 5, 3, 7, 3, 4)
for i in tup1:
    if tup1.count(i) > 1 and i not in l:
        l.append(i)
print(l)
