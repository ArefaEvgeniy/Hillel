nums = [
    ('Jon', 15),
    ('Clarc', 7),
    ('Ban', 15),
    ('Sara', 11),
    ('Nick', 15)
]

print(sorted(nums, key=lambda x: x[1], reverse=True))
print(nums)
print(nums.sort(key=lambda x: (x[1], x[0])))
print(nums)
