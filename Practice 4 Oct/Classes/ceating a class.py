class Student:
    def __init__(self,name,no,marks):
        self.name=name
        self.no=no
        self.marks=marks
    def details(self):
        print("student name is {} \nnumber is {} \nmarks is {}".format(self.name,self.no,self.marks))

s =Student ("jatin",150256,500)
s.details()