# Insert data into dictionary
dict1 = {'A': [1000,'IT'],
         'C': [3000,'IT'],
         'B': [2000,'IT'],
         'D': [4000,'HR'],
         'E': [2000,'HR'],
         'F': [1500,'IT'],
         'G': [7000,'HR']
         }
print("{:<10} {:<10} {:<10} {:<10} {:<10}".format('Employee', 'Salary', 'Department','Next_high_Sal', 'Employee'))
l=[]
l1=[]
for i in dict1.values():
    if i[1]=='IT':
       l.append(i[0])
    else:
        l1.append(i[0])

l.sort()
l1.sort()
l.extend(l1)
next=0
for key, value in dict1.items():
    Employee=key
    Salary, Department = value
    for i in l:
        if i>Salary:
            next=i
            break
        else:
            next=Salary

    print("{:<10} {:<10} {:<15} {:<15} {:<10}".format(Employee, Salary, Department,next,Employee))

print(l)