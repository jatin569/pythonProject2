def circularly_identical(list1,list2):
    list1.extend(list1)

    for i in range(len(list1)):
        if list2 == list1[i:i+len(list2)]:
            return True
    return False

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

if circularly_identical(list1,list2):
    print("yes")
else:
    print("no")