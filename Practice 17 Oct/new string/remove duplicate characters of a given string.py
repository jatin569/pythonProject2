# remove duplicate characters of a given string

s = input("Enter string : ")
s1 = ' '
for i in s:
    if s.count(i) == 1:
       s1+=i
print(s1)