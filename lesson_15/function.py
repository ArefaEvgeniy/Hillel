def get_processes():
    data = None
    ...
    return data


def get_cpu():
    data = None
    ...
    return data


def get_fun():
    data = None
    ...
    return data


def get_memory():
    data = None
    ...
    return data


def prepare_data(pids, cpu, memory, fun):

    def get_suffix(data):
        ...
        return data

    data = []
    ...
    return data


def print_info(data):
    ...


def save_DB(data):
    ...


def main():
    while True:
        pids = get_processes()
        cpu = get_cpu()
        memory = get_memory()
        fun = get_fun()
        data = prepare_data(pids, cpu, memory, fun)
        print_info(data)
        save_DB(data)


if __name__ == '__main__':
    main()
