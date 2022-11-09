class a:
    def f1(self):
        print("A Data")
class b(a):
    def f2(self):
        a.f1(self)
        print("B Data")
class c(a):
    def f3(self):
        a.f1(self)
        print("C Data")
class d(b,c):
    def f4(self):
        b.f2(self)
        c.f3(self)
        print("D Data")
ob=d()
ob.f4()
