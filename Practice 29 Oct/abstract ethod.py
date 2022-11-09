from abc import ABC,abstractmethod
class parent(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass
class child (parent):
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        print("sum is",self.n1+self.n2)
    def sub(self):
        print("subtraction",self.n1-self.n2)
ob=child(10,20)
ob.add()
ob.sub()