class Animal:
    def f1(self):
        print("All Animals")
class Tiger(Animal):
    def f2(self):
        print("Tiger")
class Lion(Animal):
    def f3(self):
        print("Lion")
class Leopard(Animal):
    def f4(self):
        print("leopard")
ob1=Tiger()
ob2=Lion()
ob3=Leopard()
ob1.f1()
ob1.f2()
ob2.f1()
ob2.f3()
ob3.f1()
ob3.f4()


