f = open("C:/Users/Anonymous/Desktop/Text.txt",'r')
a = f.read()
d = {}
for i in a.split():
    if i in d:
        d[i]+= 1
    else:
        d[i] = 1
print(d)

# other method
counts={}
f = open("C:/Users/Anonymous/Desktop/Text.txt",'r')
for line in f:
    for word in line.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
print(counts)