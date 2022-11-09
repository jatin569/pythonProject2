class Student:
  def __init__(self,name,age,rollno):
    self.name=name
    self.age=age
    self.__rollno=rollno# hiding rollno

  def details(self):
    print(self.name,self.age,self._Student__rollno)
s=Student('jatin',24,1540546)
print(s._Student__rollno)#name mangaling
s.details()