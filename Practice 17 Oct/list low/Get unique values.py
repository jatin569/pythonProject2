# Get unique values

l = [1, 5, 3, 2, 3, 1, 4, 7, 8]
for i in l:
    if l.count(i) == 1:
        print(i)