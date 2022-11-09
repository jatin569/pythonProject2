class myclass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print("please enter atleast two or three arguments")
ob=myclass()
ob.sum(10,20,30)
ob.sum(10.5,20.6)
ob.sum(15)