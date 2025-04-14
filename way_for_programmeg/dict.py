

a = (('country', 'USA'), ('language', 'English'))
named_dict = dict(a) # named_dict будет {'country': 'USA', 'language': 'English'}
print(named_dict)

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# zipped_dict = dict(zip(keys, values)) # zipped_dict будет {'a': 1, 'b': 2, 'c': 3}
#
# keys = ['x', 'y', 'z']
# new_dict = dict.fromkeys(keys) # new_dict будет {'x': None, 'y': None, 'z': None}
# value = 0
# another_dict = dict.fromkeys(keys, value) # another_dict будет {'x': 0, 'y': 0, 'z': 0}

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2) # dict1 теперь {'a': 1, 'b': 3, 'c': 4}

dict3 = {'d': 5}
dict1.update(d=6, e=7) # dict1 теперь {'a': 1, 'b': 3, 'c': 4, 'd': 6, 'e': 7}

pairs = [('f', 8), ('g', 9)]
dict1.update(pairs) # dict1 теперь {'a': 1, 'b': 3, 'c': 4, 'd': 6, 'e': 7, 'f': 8, 'g': 9}