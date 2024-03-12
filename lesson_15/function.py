import time


def get_processors():
    res = None
    ...
    return res


def get_cpu():
    res = None
    ...
    return res


def get_memory():
    res = None
    ...
    return res


def get_fun():
    res = None
    ...
    return res


def prepafre_data(pids, cpu, memory, fun):
    def print_suffix(value):
        ...
        return value

    data = None
    ...
    return data


def print_data(data):
    ...


def main():
    while True:
        pids = get_processors()
        cpu = get_cpu()
        memory = get_memory()
        fun = get_fun()
        data = prepafre_data(pids, cpu, memory, fun)
        print_data(data)
        time.sleep(1)


if __name__ == '__main__':
    main()
