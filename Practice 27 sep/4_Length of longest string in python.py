#Length of longest string in python
list1=["amit","stringgggg","towqeer"]
print(max(list1,key=len))

l=0
s=""
for i in list1:
    if len(i)>l:
        l=len(i)
        s=i
print(s)


print("..............end..................")