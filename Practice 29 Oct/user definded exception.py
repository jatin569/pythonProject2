class divide(Exception):
    pass
try:
    n1 = int(input("enter first number"))
    n2 = int(input("enter 2nd number"))
    if n2==0:
        raise divide("none")
except divide as e:
    print(e)
else:
    print("i'm jatin")
finally:
    print("over")
ob=divide(n1,n2)
