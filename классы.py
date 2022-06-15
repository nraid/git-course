# class Dog:
#
#     def __init__(self, age=4, name='Rex'):
#         self.age = age
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
#         return 'Dog(age={age}, name={name})'.format(age=self.age, name=self.name)
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#     def __eq__(self, other):
#         return self.age == other.age
#
#     def say_gav(self):
#         print(self.age)
#
#
# d1 = Dog(age=5)
# d2 = Dog(age=6)
#
#
# print(d1 == d2)
#
# -----------------------------------------------------------------------------------


class Building:

    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length
        self.volume = self.height * self.width * self.length

    def __str__(self):
        return f'{self.__class__.__name__}'  # f"This is a building that has height = {self.height}, width =
        # {self.width}, length = {self.length}."

    def __lt__(self, other):
        return self.volume < other.volume

    def __le__(self, other):
        return self.volume >= other.volume

    def __eq__(self, other):
        return self.volume == other.volume


b1 = Building(height=20, width=10, length=5)
b2 = Building(height=20, width=10, length=9)

print(b1)

