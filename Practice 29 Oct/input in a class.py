class employee:
    def set(self,name):
        self.name=name
    def get(self):
        return name
    def setid(self,eid):
        self.eid = eid
    def getid(self):
        return eid
i=0
l=[]
n=int(input("Enter number of data"))
em=employee()
while i<n:
    name=input("Enter name")
    eid=input("enter id")
    em.set(name)
    em.setid(eid)
    l.append(name)
    l.append(eid)
    i+=1
print(l)


