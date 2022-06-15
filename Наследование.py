# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#
#     def eat(self, food):
#         print('eating...')
#
#     @abstractmethod
#     def sound(self):
#         pass
#
#
# class Dog(Animal):
#
#     def sound(self):
#         print("Gav gav....")
#
#
# class Cat(Animal):
#
#     def sound(self):
#         print("Meow...")
#
#
# d = Dog()


class Predator:

    def __init__(self, name, age, hours):
        self._name = name
        self._age = age
        self._hours = hours

    def kinut_ponti(self):
        print('How brilliant i am.')


class Diamond(Predator):

    def samozvanec(self):
        print("A tochno li ya igrau na diamond...")


class Platinum(Diamond):

    def garbage(self):
        print("Pohody ya mysor")

    def kinut_ponti(self):
        print("IM ROLLLINNGGGG")


pred = Predator('Ivan', 24, 200)
almaz = Diamond('Kaliman', 28, 500)
plat = Platinum('Artem', 45, 2000)


pred.kinut_ponti()
almaz.samozvanec()
plat.garbage()
plat.kinut_ponti()

