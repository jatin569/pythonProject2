# strip a set of characters from a string

str1 = input("Enter string : ")
s = 'aeiou'
s2=''
for i in str1:
    if i in s:
        pass
    else:
        s2=s2+i


print(s2)

#other method
def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)
n=input("Enter string: ")
print(strip_chars(n, "aeiou"))
