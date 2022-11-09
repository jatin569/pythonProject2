class Student:
  def __init__(self,name,age,rollno):
    self.name=name
    self.age=age
    self.rollno=rollno

  def details(self):
    print(self.name,self.age,self.rollno)
s=Student('jatin',24,1540546)
s.details()