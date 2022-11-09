class Animal:
    def f1(self):
        print("All Animal")
class Tiger(Animal):
    def f2(self):
        print("Tiger")
class lion(Animal):
    def f3(self):
        print("Lion")
class Leopard(Animal):
    def f4(self):
        print("Leopard")
ob1=Tiger()
ob2=lion()
ob3=Leopard()
ob1.f1()
ob1.f2()
ob2.f1()
ob2.f3()
ob3.f1()
ob3.f4()