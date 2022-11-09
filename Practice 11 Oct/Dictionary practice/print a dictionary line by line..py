#print a dictionary line by line.

cars = {'A':{'speed':70,'color':2},'B':{'speed':60,'color':3}}
for i in cars:
    print(i)
    for j in cars[i]:
        print(j, ':', cars[i][j])
