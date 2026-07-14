# Написати функцію, яка повертає true, якщо у списку йде поспіль два
# рази задане число.
# Якщо задане число 2, то [1, 2, 2] -> true, [2, 1, 2] -> false


def has_two_consecutive(nums, target):
    for i in range(len(nums) - 1):
        if nums[i] == target == nums[i+1]:
            return True
    return False


a = [1, 2, 3, 7, 4, 5, 6, 7, 7, 8, 9]
print(has_two_consecutive(a, int(input('Enter your number: '))))
