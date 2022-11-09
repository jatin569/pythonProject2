#to reverse a string

def reverse(s):
    return s[::-1]
s="Jatin"
print("Reversed string:",reverse(s))
#other mthod


def rev(s1):
    str=""
    for i in s1:
        str=i+str
    return str
s1=("Dhiman")
print("Reversed string:",rev(s1))