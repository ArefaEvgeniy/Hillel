def func(a="variant 1"):
    def qq(word="step"):
        return word.title() + "!"

    def ww(word="wood"):
        return word.lower() + "..."

    if a == "variant 2":
        res = qq
    else:
        res = ww

    return res


print(func)
result = func()
print(result)
print(result())

print('-' * 100)
result = func("variant 2")
print(result)
print(result("ulia"))

print('-' * 100)
result = func("variant 1")
print(result)
print(result(word="ulia"))
