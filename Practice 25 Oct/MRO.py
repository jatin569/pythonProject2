class A:
    def __init__(self):
        print("jatin")
        super().__init__()
class B:
    def __init__(self):
        print("Dhiman")
        #super().__init__()
class C(A,B):
    def __init__(self):
        print("towqeer")
        super().__init__()
ob=C()

