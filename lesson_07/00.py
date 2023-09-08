def read_data():
    data = None
    ...
    return data


def verify(data):
    result = True
    ...
    return result


def process(data):
    new_data = None
    ...
    return new_data


def send_data(data):
    ...


def main():
    input_data = read_data()
    if not verify(input_data):
        exit(1)

    new_data = process(input_data)
    send_data(new_data)


main()
