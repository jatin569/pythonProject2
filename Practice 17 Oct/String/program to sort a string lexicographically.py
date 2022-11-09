#program to sort a string lexicographically

def lexicographically(s):
    return sorted(sorted(s),key=str.upper)
print(lexicographically("Jatin"))

#without function
a=sorted(("Dhiman"),key=str.upper)
print(a)