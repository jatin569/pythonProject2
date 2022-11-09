class Father:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def show(self):
        print("Father's name is",self.name,self.surname)
class Child(Father):
    def child_details(self,name):
        print("child name is",name,self.surname)
ob=Child("jatin","Dhiman")
ob.show()
ob.child_details("Amit")