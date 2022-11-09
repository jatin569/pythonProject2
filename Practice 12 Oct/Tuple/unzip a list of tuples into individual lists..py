# unzip a list of tuples into individual lists.
l=[]
tup=((1,2,3),(4,5,6),(7,8,9))
for i in tup:
    for j in i:
       l.append(j)
print(l)