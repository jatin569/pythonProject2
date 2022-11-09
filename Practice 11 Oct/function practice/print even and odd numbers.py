#print even and odd numbers

def even_odd(n):
    for i in range(n):
        if i%2==0:
            print(i,'even')
        else:
            print(i,'odd')
even_odd(50)
