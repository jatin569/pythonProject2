class duck:
    def talk(self):
        print("quack quack")
class horse:
    def talk(self):
        print("chbcb")

def myfun(obj):
    obj.talk()
d=duck()
myfun(d)
