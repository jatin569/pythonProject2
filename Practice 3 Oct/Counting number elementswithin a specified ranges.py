l=[5,4,6,15,23,56,28,96]
start=10
end=60
count=0
for i in l:
    if start <= i <= end:
        count+=1
print(count)
