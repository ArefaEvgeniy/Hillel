class MyStr(str):
    def __iter__(self):
        self.data = self.split()
        self.current = -1
        return self

    def __next__(self):
        self.current += 1
        if self.current < len(self.data):
            return self.data[self.current].replace('.', '').replace(',', '').replace(':', '').title()
        raise StopIteration


data = MyStr("RRETgdf xfx dfg drret, fh: nfgd dfseter xcbfgdgdf.")

for item in data:
    print(item)
