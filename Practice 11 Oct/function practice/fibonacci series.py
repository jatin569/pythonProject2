#fibonacci series

def fibonacci(n):
    n1=0
    n2=1
    temp=0
    for i in range(1,n):
        print(n1)
        temp=n1+n2
        n1=n2
        n2=temp
fibonacci(10)