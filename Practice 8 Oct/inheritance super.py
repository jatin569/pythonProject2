class parent():
    def __init__(self,id,name,Add):
        self.id=id
        self.name=name
        self.Add=Add
class child(parent):
    def __init__(self,id,name,Add,email):
        super().__init__(id,name,Add)
        self.email=email
    def details(self):
        print(self.id,self.name,self.Add,self.email)
ob=child(1,'jatin','chd','hdbh@')
ob.details()