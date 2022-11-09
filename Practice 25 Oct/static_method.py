class Myclass:
    n = 0

    def __init__(self):
        Myclass.n = Myclass.n + 1

    @staticmethod
    def show(a,b):
        print("No of instance created:", Myclass.n,"\nsum of elements is: ",a+b)


ob1 = Myclass()
ob2 = Myclass()
ob3 = Myclass()
Myclass.show(10,20)


