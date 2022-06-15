class Dog:

    def __init__(self, age=4, name='Rex'):
        self.age = age
        self.name = name
        self._hearth = 'Big hearth'

    def __open_mouth(self):
        print("Opening...")

    def _give_sound(self):
        print("GAV GAV.")

    def _close_mouth(self):
        print("Closing...")

    def say_gav(self):
        self.__open_mouth()
        self._give_sound()
        self._close_mouth()


d = Dog()
d.say_gav()

