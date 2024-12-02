class Dog:
    color = "Black"

    def speak(self):
        return "Woof!"


class Cat(object):
    def speak(self):
        return "Meow!"


def animal_sound(animal):
    return animal.speak()


# dog_1 = Dog()
# dog_2 = Dog()
# dog_3 = Dog()
#
# print(dog_1)
# print(dog_3)
#
# print(dog_1.speak())
#
# my_str_1 = 'line 1'
# my_str_2 = str('line 2')
#
# print(my_str_1)
# print(my_str_2)

dog_instance = Dog()
cat_instance = Cat()
# print(dog_instance.speak())
# print(cat_instance.speak())

print(animal_sound(dog_instance))  # Вивід: Woof!
print(animal_sound(cat_instance))  # Вивід: Meow!
