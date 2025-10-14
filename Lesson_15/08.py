class MyString(str):
    def __iter__(self):
        self.string = self.split()
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.string):
            word = self.string[self.index].replace(".", "").replace(",", "").replace("!", "")
            self.index += 1
            return word.title()
        else:
            raise StopIteration


data = MyString("I love PYTHON. I love programming. I love coding, too!")

for item in data:
    print(item)
