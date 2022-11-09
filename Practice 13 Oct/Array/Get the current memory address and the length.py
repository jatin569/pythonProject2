# Get the current memory address and the length in elements of the buffer used to hold an arrays?
# contents and also find the size
from array import *
arr = array('i', [1, 3, 5, 7, 9])

print("Current memory address and the length in elements of the buffer: "+str(arr.buffer_info()))
print("The size of the memory buffer in bytes: "+str(arr.buffer_info()[1] * arr.itemsize))
