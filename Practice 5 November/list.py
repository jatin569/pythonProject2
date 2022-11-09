strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = [[], [], []]
for i in strs:

    if sorted(i) == sorted("bat"):
        output[0].append(i)

    elif sorted(i) == sorted("nat") or sorted(i) == sorted("tan"):
        output[1].append(i)

    else:
        output[2].append(i)

print(output)
my_list = [[1, 2, 3], [4, 5,[ 6, 7]],8]
new = []
for i in my_list:
    if type(i)==int:
        new.append(i)
    else:
        for j in i:
            if type(j)==list:
                for k in j:
                    new.append(k)
            else:
                new.append(j)
        
print(new)