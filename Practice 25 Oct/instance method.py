class student:
    def __init__(self,name='',marks=0):
        self.name=name
        self.marks=marks
    def display(self):
        print("Hi",self.name)
        print('your marks',self.marks)
    def calculate(self):
        if (self.marks>600):
            print("you got first grade")
        elif(self.marks>=500):
            print("you got second grade")
        elif(self.marks>=350):
            print("you got 3rd grade")
        else:
            print("you got failed")
n=int(input("How many students?"))
i = 0
dic = {}
while i < n:
    name = input("Enter name : ")
    marks = int(input("enter marks : "))
    s = student(name, marks)
    dic.update({name : marks})
    s.display()
    s.calculate()
    i += 1
print(dic)