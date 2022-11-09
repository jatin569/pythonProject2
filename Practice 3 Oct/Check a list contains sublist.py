l=[5,3,6,8,2,6,9]
sub_list=[2,8,5]
for i in range(len(sub_list)):
    if sub_list[i] not in l:
        print("Its not sulist")
        break
else:
    print("sublist")