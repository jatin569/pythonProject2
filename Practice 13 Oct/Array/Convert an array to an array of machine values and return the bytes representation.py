# Convert an array to an array of machine values and return the bytes representation

from array import *
arr = array('b', [1, 3, 5, 7, 9, 5])

s=arr.tobytes()
print(s)