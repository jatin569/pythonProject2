# to display a number in left, right and center aligned of width 10
x=int(input("Enter number: "))

print('left {:<10d}'.format(x))
print('Right {:10d}'.format(x))
print('Center {:^10d}'.format(x))