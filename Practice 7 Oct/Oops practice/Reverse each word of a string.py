#Reverse each word in a string
def reverse(s):
    a=s.split()
    for i in a:
        print(i[::-1],end=" ")
reverse("My name is jatin")


