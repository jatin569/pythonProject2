
f = open("C:/Users/Anonymous/Desktop/Git/data.txt",'r')
a= f.read()
d={}
for i in a.split():
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)


