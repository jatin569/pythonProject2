# Counting number elements within a specified ranges

list1 = [10, 15, 20, 40, 13, 45, 27]
num1 = int(input("Enter first number : "))
num2 = int(input("Enter 2nd number : "))
c=0
for i in range(num1, num2+1):
    if i in list1:
        c+= 1
print(c)


#other method
def count(li, min, max):
    ctr = 0
    for i in li:
        if min <= i <= max:
            ctr += 1
    return ctr

list2 = [10,20,30,40,40,40,70,80,99]
print(count(list2, 40, 100))
