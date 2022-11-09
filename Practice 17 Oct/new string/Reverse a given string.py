# Reverse a given string  Input : "Python"   Output : "nohtyP"

s = 'Python'
a = ''
for i in range(len(s)):
    a = a+s[-i-1]
print(a)