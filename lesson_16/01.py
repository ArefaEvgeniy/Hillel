nums = [
    ('Jon', 15),
    ('Clarc', 7),
    ('Ban', 18),
    ('Sara', 7),
    ('Nick', 7)
]

print(sorted(nums, key=lambda x: x[1], reverse=True))

nums.reverse()
print(nums)

print(sorted(nums, key=lambda x: (x[1], x[0])))
