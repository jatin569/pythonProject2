class sample:
     x=10

     @classmethod
     def modify(cls):
         cls.x+=1
s1=sample()
s2=sample()
print(s1.x)
print(s2.x)

s1.modify()
print(s1.x)
print(s2.x)
