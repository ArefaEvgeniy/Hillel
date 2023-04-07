class MyException(Exception):
    def __init__(self, message='First value lesser then second value'):
        super().__init__(message)


raise MyException
