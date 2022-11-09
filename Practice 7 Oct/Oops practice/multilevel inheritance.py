class Animal:
    def f1(self):
        print("All Animal")
class Wild_Animal(Animal):
    def f2(self):
        print("wild animal")
class Tiger(Wild_Animal):
    def f3(self):
        print("Tiger")
t=Tiger()
t.f1()
t.f2()
t.f3()