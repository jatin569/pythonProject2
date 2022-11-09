n=int(input("Enter number:"))

def fun(i):
    a=(n,'X',i,'=',n*i)
    return a
for  i in range(1,11):
    print(fun(i))

#another method
def fun(n):

    for i in range(1,11):
        a=(n,'X',i,'=',n*i)
        print(a)
    return a
fun(n)

