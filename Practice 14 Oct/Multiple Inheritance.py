class A:
    def f1(self):
        print("Father")
class B:
    def f2(self):
        print("mother")
class C(A,B):
    def f3(self):
        print("Child")
ob=C()
ob.f1()
ob.f2()
ob.f3()