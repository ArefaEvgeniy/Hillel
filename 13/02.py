try:
    x = 0
    assert x > 0, "Hello, world"
except AssertionError:
    x = 1

print('continue')
print(f'x: {x}')
...
