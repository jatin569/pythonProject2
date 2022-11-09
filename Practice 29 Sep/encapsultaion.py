class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def display(self):
        print('Name is',self.name)
        print('Age is',self.age)
        print('Marks',self.marks)

s=student("Jatin",20,599)
s.display()