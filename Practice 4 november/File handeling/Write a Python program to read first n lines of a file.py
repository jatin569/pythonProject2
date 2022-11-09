# Write a Python program to read first n lines of a file

# f = open("C:/Users/Anonymous/Desktop/Git/data.txt",'r')
# print(f.read())
from itertools import islice

with open("C:/Users/Anonymous/Desktop/Git/data.txt") as myfile:
    for line in islice(myfile, 10):
        print(line.strip())