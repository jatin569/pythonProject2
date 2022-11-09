class employee:
    def __int__(self,age):
        self.name=age
    def __init__(self, id, name, salary):
        self.id=id
        self.name=name
        self.salary=salary

    def show(self):
        print(self.id,self.name,self.salary)
em=employee(1,"jatin",150000)
em.show()

# other example
class Student:
    # one argument constructor
    def __init__(self, name):
        print("One arguments constructor")
        self.name = name

    # two argument constructor
    # def __init__(self, name, age):
    #     print("Two arguments constructor")
    #     self.name = name
    #     self.age = age

# creating first object
emma = Student('Emma')

# creating Second object
kelly = Student('Kelly', 13)
