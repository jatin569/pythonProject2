#Issubset and issuperset.

s={1,2,3,4,5,6}
s1={2,4,6}

if s1.issubset(s):
    print("is subset")
else:
    print("not subset")

if s.issuperset(s):
    print("is a superset")
else:
    print("not superset")