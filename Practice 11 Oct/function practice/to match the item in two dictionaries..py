# to match the item in two dictionaries.


def matching(d1, d2):
    for key, value in d1.items():
        for k, v in d2.items():
            if key == k and value == v:
                print(key,d1.get(key))

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'e': 5, 'a': 1, 'b': 2, 'f': 6}
matching(dict1, dict2)
