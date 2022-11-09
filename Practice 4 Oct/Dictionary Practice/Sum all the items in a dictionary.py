dict1={'a':100,'b':200,'c':300}
sum=0
for i in dict1:
    sum=sum+dict1.get(i)
print("sum of dictionary items is:",sum)