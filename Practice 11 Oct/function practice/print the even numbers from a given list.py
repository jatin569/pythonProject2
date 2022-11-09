#print the even numbers from a given list
def even(l):
    for i in l:
        if i%2==0:
            print(i)
l=[3,5,7,6,45,4,2,10,1,8]
even(l)