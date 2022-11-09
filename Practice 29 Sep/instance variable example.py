
class sample:
    def __init__(self):
        self.x=10

    def modify(self):
        self.x+=1

s1=sample()
s2=sample()
print('x in S1=',s1.x)
print('x in S2=',s2.x)

s1.modify()
print('x in S1=',s1.x)
print('x in S2=',s2.x)

