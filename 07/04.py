from collections import defaultdict


input_list = ['r', 66, 99, 'e', 66, 'r', 't', 66, 'r', 't', 'n', 'r']
def_dict = defaultdict(lambda: 0)
my_dict = {}

for item in input_list:
    if my_dict.get(item) is None:
        my_dict.update({item: 1})
    else:
        my_dict[item] += 1

for item in input_list:
    def_dict[item] += 1

print(my_dict)
print(def_dict)

print(def_dict['RRR'])
print(def_dict)
