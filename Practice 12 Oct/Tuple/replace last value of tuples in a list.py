# replace last value of tuples in a list
l = [(2, 5, 1), (6, 4, 8)]
print([t[:-1] + (100,) for t in l])


#other method
d=[]
for i in l:
    d.append(i[:-1]+(100,))
print(d)
