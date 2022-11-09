# find the first repeated word in a given string

n = input("Enter String : ")
a = n.split()

for i in a:
    if a.count(i)>1:
        print(i)
        break
else:
    print('none')