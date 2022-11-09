#remove leading zeros from an IP address
n='123.00640.057'
a=n.split('.')
print(a)
x=[int(i) for i in a]
y=[str(i) for i in x]
s=".".join(y)
print(s)

