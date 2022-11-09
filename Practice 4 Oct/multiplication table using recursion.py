def table(n,i):
    if i>10:
        return
    print(n,"X",i,'=',n*i)
    return table(n,i+1)
n=int(input("enter number: "))

table(n,1)