# Frequency of elements

list1 = [25, 10, 15, 10, 15, 20, 15, 25, 30]

dict1 = {}

for i in list1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

print(dict1)

#other method

import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]

print("Original List : ", my_list)
ctr = collections.Counter(my_list)

print("Frequency of the elements in the List : ", ctr)