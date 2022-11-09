# sum all the numbers in a list
def sum(l):
    s=0
    for i in l:
        s=s+i
    return s
l=[1,2,3,4,5,6,7,8]
print(sum(l))