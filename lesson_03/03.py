import copy

input_list = [1, 'a', 4, None, ['d', 'x', 99]]  #  112314, 12432423, 54545342, 6e6436346, 34634634

first_list = input_list[:]                      #  112314, 12432423, 54545342, 6e6436346, 34634634
second_list = copy.copy(input_list)             #  112314, 12432423, 54545342, 6e6436346, 34634634
therd_list = copy.deepcopy(input_list)          #  112314, 12432423, 54545342, 6e6436346, 669080358

print('0:', input_list)
print('1:', first_list)
print('2:', second_list)
print('3:', therd_list)
print('-' * 50)

first_list.append('new')
second_list.pop(0)
second_list[-1].append(0)

print('0:', input_list)
print('1:', first_list)
print('2:', second_list)
print('3:', therd_list)
