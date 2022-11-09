#program to check whether a string starts with specified characters

str=input("Enter a string: ")
if str.startswith('@'):
    print("String starts with special character")
else:
    print("its not starts with special character")

#to print the following floating numbers upto 2 decimal places
a=float(input("enter number: "))
print(round(a,2))

#print the following floating numbers upto 2 decimal places with a sign
l=123.485
print("{:+.2f}".format(l))