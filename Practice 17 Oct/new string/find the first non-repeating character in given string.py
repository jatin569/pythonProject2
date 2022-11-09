# find the first non-repeating character in given string

s=input("Enter String : ")

for i in s:
    if s.count(i)==1:
        print(i)
        break
else:
    print('none')
