# print all permutations with given repetition number of given string

from itertools import product
def all_repeat(str1, rno):

    chars = list(str1)
    results = []
    for i in product(chars, repeat = rno):
        results.append(i)
    return results

print(all_repeat('xyz',3))


