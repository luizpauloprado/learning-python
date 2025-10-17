# Inheritance
# Define a class named Animal
class Animal:
    def __init__(self, name: str):
        self.name: str = name

    def speak(self):
        print("Nothing to speak")

    def get_name(self):
        print(self.name)


# Define a subclass named Dog that inherits from the Animal class
class Cat(Animal):
    # Override the speak method of the Animal clas
    def speak(self):
        print("overrided speak() = meow")


animal: Animal = Animal("Animal")
animal.speak()
animal.get_name()

cat: Cat = Cat("Garfield")
cat.speak()
cat.get_name()
