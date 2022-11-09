my_list = [[1, 2, 3], [4, 5,[6, 7]]],8

def flat(lst):
    output = []
    for item in lst:
        if type(item) == list:
            output = output + flat(item)
        else:
            output.append(item)
    return output

print(flat(my_list))

