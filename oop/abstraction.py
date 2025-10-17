# Abstraction

# Abstraction can be achieved by using abstract classes or interfaces.
# An abstract class is a class that cannot be instantiated directly,
# but is meant to be subclassed by other classes.

# It often includes abstract methods that have no implementation,
# but provide a template for how the subclass should be implemented.

# This allows the programmer to define a common interface for a group of related classes, while still allowing each class to have its own specific behavior.

# !!! Python does not have built-in support for abstract classes or interfaces !!!
# can be implemented using the abc (abstract base class) module

# Import the abc module to define abstract classes and methods
from abc import ABC, abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass


# Define a Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implement the area method for Rectangles
    def area(self):
        return self.width * self.height


# Define a Circle class that also inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implement the area method for Circles
    def area(self):
        return 3.14 * self.radius**2


# Create a list of shapes that includes both Rectangles and Circles
shapes = [Rectangle(4, 5), Circle(7)]

# Loop through each shape in the list and print its area
for shape in shapes:
    print(shape.area())
