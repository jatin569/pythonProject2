class A:
    def f1(self):
        print("Grandfather")
class B(A):
    def f2(self):
        print("Father")
class C(B):
    def f3(self):
        print("Child")
obj=C()
obj.f1()
obj.f2()
obj.f3()