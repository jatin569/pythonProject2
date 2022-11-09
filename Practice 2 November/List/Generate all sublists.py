# Generate all sublists

l = [10, 3, 2, 5, 1, 11, 4, 77, 8]

l1 = []
for i in range(len(l)+1):
    for j in range(i):
        l1.append(l[j:i])
print(l1)