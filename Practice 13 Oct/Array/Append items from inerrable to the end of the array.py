# Append items from inerrable to the end of the array
from array import *
arr = array('i', [1, 3, 5, 7, 9, 5])


arr.extend(arr)
print(arr)