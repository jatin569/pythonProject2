# count the elements in a list until an element is a tuple

l = [1, 2, 3, 4, 5, 6, (7, 8)]
count = 0
for i in l:
    if type(i) == tuple:
        break
    count += 1
print(count)
