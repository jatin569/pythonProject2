class person:
    def __init__(self,name,age):
        self.__name=name## with __ we are hiding variable
        self.age=age

    def talk(self):
        print(self._person__name)#with _classname__variable name we are unhiding the data
        print(self.age)
p=person('jatin',25)
#print(p._person__name)

p2=person("towqeer",45)
p.talk()
p2.talk()