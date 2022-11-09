# to remove an empty tuple(s) from a list of tuples
l = ((2, 5, 1), (1,2), (6, 4, 8), (), ())
d = []
for i in l:
    if len(i) >= 1:
        d.append(i)
d=tuple(d)
print(d)