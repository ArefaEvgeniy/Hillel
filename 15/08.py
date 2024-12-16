# Приклад менеджера контекста для відкриття файлу


class FileManager:
    def __init__(self, file_name, mode='r', encoding='utf-8'):
        self.file_name = file_name
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"Exception occurred: {exc_type}, {exc_value}")
            return False  # Виключення не обробляється і передаєтьься далі
        return True


# Використання нашого менеджера контексту
with FileManager("cleaned.txt", "r") as file:
    content = file.read()
    print(content)
