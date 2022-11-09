# Append items from a specified list.

from array import *
arr = array('i', [1, 3, 5, 7, 9, 5])
a = [5, 6, 7, 8]
for i in a:
    arr.append(i)
print(arr)