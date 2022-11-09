num_list=[10,20,30,40,50,60,70,80,90,100]
a=[]
for i in range(0,len(num_list)):
    if num_list[i]>50:
        del num_list[i]
print(num_list)