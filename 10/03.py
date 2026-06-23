def my_func(word="shout"):
    def shout(word="stop"):
        return word.upper() + "!"

    def whisper(word="stop"):
        return word.lower() + "..."

    if word == "shout":
        return shout
    else:
        return whisper


maxim = my_func()
print(maxim("Maxim"))
print(my_func("ggg")("start"))
