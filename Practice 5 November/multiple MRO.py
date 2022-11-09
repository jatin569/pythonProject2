

class A:
    def __init__(self):
        print("A")
        super().__init__()
class B:
    def __init__(self):
        print("B")
        super().__init__()
class c(A,B):

    def __init__(self):
        print("C")
        super().__init__()
ob=c()