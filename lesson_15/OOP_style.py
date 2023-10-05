class Abstract_Class:
    def get(self):
        pass

    def prepare(self):
        ...

    def print(self):
        ...


class Cpu(Abstract_Class):
    def get(self):
        ...


class Memory(Abstract_Class):
    def get(self):
        ...


class Processors(Abstract_Class):
    def get(self):
        ...


class Temperatures(Abstract_Class):
    def get(self):
        ...


def main():
    info = (Cpu(), Memory(), Processors(), Temperatures())
    while True:
        for item in info:
            item.get()
            item.prepare()
            item.print()


if __name__ == '__main__':
    main()
