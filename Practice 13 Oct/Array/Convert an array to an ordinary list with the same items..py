# Convert an array to an ordinary list with the same items.

from array import *
arr = array('i', [1, 3, 5, 7, 9, 5])

arr=list(arr)
print(arr,type(arr))