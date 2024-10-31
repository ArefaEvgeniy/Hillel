first_list = [2, 4, 7, 11, 0, -2, 8]
print(min(first_list))  # -2


second_list = ['2', 'Hello', '7777777', 'word', "red"]
print(min(second_list))
print(max(second_list))
second_list.sort()
print(second_list)


print(all([1, True, 10]))  # True
print(all([4 > 2, True, 5 == 5]))  # True
print(all([4 > 2, True, 5 != 5]))  # False

print('-' * 100)

print(any([False, 1 == 1, False]))  # True
print(any([]))   # False
print(any([False, 0, '', 1 > 1]))  # False
print(any([False, 0, 'rt', 1 > 1]))  # True
print(all([]))  # True Будьте обережні!
