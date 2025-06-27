def func(choice="shout"):
    def shout(word="yes"):
        return f"{word.upper()}!"

    def wishper(word="yes"):
        return f"{word.lower()}..."

    if choice == "shout":
        return shout
    else:
        return wishper


print(func("RRR")("TeTiAnA"))
print(func()("TeTiAnA"))
