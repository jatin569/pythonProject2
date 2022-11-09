class Student:
    def setname(self, name):
        self.name = name

    def getname(self):
        return name

    def setmarks(self, marks):
        self.marks = marks

    def getmarks(self):
        return marks

n = int(input("How many students: "))

dic = {}
s = Student()
i = 0
while i < n:
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    s.setname(name)
    s.setmarks(marks)

    dic.update({name : marks})
    print("Hi", s.getname())
    print("Your marks is :",s.getmarks())
    i += 1
print(dic)
