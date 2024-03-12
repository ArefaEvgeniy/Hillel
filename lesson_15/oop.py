import time


class AbstractClass:
    def get(self):
        ...

    def prepare(self):
        ...

    def print(self):
        ...


class Cpu(AbstractClass):

    def get(self):
        ...

    def prepare(self):
        super().prepare()
        ...


class Memory(AbstractClass):

    def get(self):
        ...

    def prepare(self):
        super().prepare()
        ...


class Fun(AbstractClass):

    def get(self):
        ...

    def prepare(self):
        super().prepare()
        ...

    def print(self):
        ...


class Processes(AbstractClass):

    def get(self):
        ...

    def prepare(self):
        ...

    def print(self):
        ...


def main():
    info = (Cpu(), Memory(), Processes(), Fun())
    while True:
        for item in info:
            item.get()
            item.prepare()
            item.print()
        time.sleep(1)


if __name__ == '__main__':
    main()