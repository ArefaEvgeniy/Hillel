class AbstractClass:
    def get(self):
        ...

    def prepare(self):
        ...

    def print(self):
        ...

    def save_DB(self):
        ...


class Cpu(AbstractClass):
    ...


class Memory(AbstractClass):
    ...


class Processes(AbstractClass):
    ...


class Fun(AbstractClass):
    ...


def clear_monitor():
    ...


def main():
    info = (Cpu(), Memory(), Processes(), Fun())
    while True:
        for item in info:
            item.get()
            item.prepare()
            item.print()
            item.save_DB()

        clear_monitor()


if __name__ == '__main__':
    main()
