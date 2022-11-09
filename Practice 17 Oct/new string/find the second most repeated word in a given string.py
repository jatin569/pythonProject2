# find the second most repeated word in a given string

n = input("Enter String : ")
a = n.split()
s=[]
for i in a:
    if a.count(i)>1 and i not in s:
        s.append(i)
print(s[1])
