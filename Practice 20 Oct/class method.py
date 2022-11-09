from datetime import date
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birthyear):
        return cls(name, date.today().year-birthyear)
    def show(self):
        print(self.name, self.age)

# ob = student("jessa", 20)
# ob.show()
joy = student.calculate_age("Joy", 1995)
joy.show()