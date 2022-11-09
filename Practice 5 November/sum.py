class Base1:
    def __init__(self):
        self.str1 = 10
        # print("Base1")


class Base2:
    def __init__(self):
        self.str2 = 20
        # print("Base2")


class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        # print("Derived")

    def printStrs(self):
        print(self.str1 + self.str2)


ob = Derived()
ob.printStrs()



