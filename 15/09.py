class MyIterator:
    def __init__(self, data:str):
        self.data = data.split()
        self.current = -1

    def __next__(self):
        self.current += 1
        if self.current < len(self.data):
            return self.data[self.current].replace('.', '').replace(',', '').replace(':', '').title()
        raise StopIteration


class MyStr(str):
    def __iter__(self):
        return MyIterator(self)


data = MyStr("RRETgdf xfx dfg drret, fh: nfgd dfseter xcbfgdgdf.")

for item in data:
    print(item)
