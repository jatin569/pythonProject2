# Check a list contains sublist

list1 = [10,25,20,1,4,5]

sub_list = [1,20,4,2]
for i in sub_list:
    if i not in list1:
        print("not sublist")
        break
else:
    print('sublist')
