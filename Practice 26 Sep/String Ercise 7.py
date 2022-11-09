#Exercise 6: Create a mixed String using the following rules

n1=input("enter string:")
n2=input("enter string:")
s=""
s1_length = len(n1)
s2_length = len(n2)
n2=n2[::-1]
length = s1_length if s1_length > s2_length else s2_length
for i in range(0,length):
        if i<s1_length:
            s=s+n1[i]
        if i<s2_length:
            s=s+n2[i]
print(s)
