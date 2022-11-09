class A:
    def f1(self):
        print("A")
class B(A):
    def f2(self):
        A.f1(self)
        print("B")
class C(A):
    def f3(self):
        A.f1(self)
        print("C")
class D(B,C):
    def f4(self):
        B.f2(self)
        C.f3(self)
        print("D")
obj=D()
obj.f4()