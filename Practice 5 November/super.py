class student:
    def __init__(self,name,rollno,address):
        self.name=name
        self.rollno=rollno
        self.address=address

    def show(self):
        print('name is {} rollno is {} address is'.format(self.name,self.rollno,self.address))