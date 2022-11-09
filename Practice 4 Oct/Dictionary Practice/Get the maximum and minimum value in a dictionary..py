dict1={"Ashutosh":5000,'Towqeer':4500,'Raghu':50000}

minimum=dict1.get("Ashutosh")
max=0
for i in dict1.values():
    if i<minimum:
        minimum=i
    if i>max:
        max=i
print(min,max)

#other method
a=[i for i in dict1.values()]
pri