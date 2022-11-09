# find the first repeated character of a given string where the index of first occurrence is smallest

s = input("Enter String : ")

for i in s:
    if s.count(i)>1:
        print(i,s.index(i))
        break
else:
    print('no repeated character')


