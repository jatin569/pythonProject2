# Finding a second largest number

l = [10,4,3,7,2,8,18,25,23,29]
for i in range(len(l)):
    for j in range(i, len(l)):
        if l[i]>l[j]:
            l[i], l[j] = l[j], l[i]
print(l[-2])
