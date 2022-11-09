class Mother:
    def f1(self):
        print("mother")
class Father:
    def f2(self):
        print("Father")
class Child(Mother,Father):
    def f3(self):
        print("child")
ch=Child()
ch.f1()
ch.f2()