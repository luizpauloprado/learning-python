from abc import ABC, abstractmethod


class IAnimal:
    @abstractmethod
    def speak(self):
        pass


class Dog(IAnimal):
    def __init__(self):
        self.__sound = "Auau"

    def speak(self):
        print(self.__sound)


dog = Dog()
dog.speak()
