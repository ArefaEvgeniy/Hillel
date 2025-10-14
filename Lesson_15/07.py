class MyIter:
    def __init__(self, string: str):
        self.string = string.split()  # ["I", "love", "PYTHON.", "I", "love", "programming.", "I", "love", "coding,", "too!"]
        self.index = 0

    def __next__(self):
        if self.index < len(self.string):
            word = self.string[self.index].replace(".", "").replace(",", "").replace("!", "")
            self.index += 1
            return word.title()
        else:
            raise StopIteration


class MyString(str):
    def __iter__(self):
        return MyIter(self)


data = MyString("I love PYTHON. I love programming. I love coding, too!")


for item in data:
    print(item)
