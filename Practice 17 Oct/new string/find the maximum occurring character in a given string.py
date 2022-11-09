#  find the maximum occurring character in a given string

s = input("Enter string : ")
a = {}
for i in s:
    if s.count(i)>1:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
result= max(a, key = a.get)
print(result)