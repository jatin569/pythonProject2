class car:
    color="Black"
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def show(self):
        print("Name of car is",self.name,"\nPrice of car is ",self.price)

    @classmethod
    def detail(cls):
        print("color of car is",cls.color)

    @staticmethod
    def details2(age):
        print("Age of car is",age)
c=car('gcc',7677)
c.show()
c.detail()
c.details2(10)


def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(5))