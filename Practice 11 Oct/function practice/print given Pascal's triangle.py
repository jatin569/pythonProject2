#print given Pascal's triangle

def triangle(n):
    for i in range(1,11):
        print(" "*(n-i),end=" ")
        print("* "*i)
triangle(50)