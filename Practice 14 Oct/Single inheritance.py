class A:
    def f1(self):
        print("Parent Class")
class B(A):
    def f2(self):
        print("Child Class")

obj=B()
obj.f1()