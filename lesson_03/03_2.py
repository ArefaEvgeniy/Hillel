import copy

first = [1, 2, 'f', [5, 6]]
                     #  1 - 00242424
                     #  2 - 66e4er5
                     #  f - 886445474
                     #  f - 886445474
                     # [5, 6] - 9900999
                     # first - 76732654  (00242424, 66e4er5, 886445474, 9900999)

third = copy.copy(first)
                     # third - 099848783  (00242424, 66e4er5, 886445474, 9900999)
second = copy.deepcopy(first)
                     # second - 099848783  (00242424, 66e4er5, 886445474, 6677775)

third.append(15)
print(first)
print(id(first))
print(third)
print(id(third))

third[3].pop()
print('-' * 50)
print(first)
print(id(first))
print(third)
print(id(third))
