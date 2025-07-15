def __setattr__(self, attr_name, attr_value):
    if attr_name == "age" and str(attr_value.isdigit()) and 18 <= attr_value <= 60:
        self.age = attr_value
    self.__dict__[attr_name] = attr_value

