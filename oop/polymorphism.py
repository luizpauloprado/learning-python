# The Shape class is defined with an abstract area method, which is intended to be overridden by subclasses.
class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    # The Rectangle class is defined with an __init__ method that initializes
    # width and height instance variables.
    # It also defines an area method that calculates and returns
    # the area of a rectangle using the width and height instance variables.
    def __init__(self, width, height):
        self.width = width  # Initialize width instance variable
        self.height = height  # Initialize height instance variable

    def area(self):
        return self.width * self.height  # Return area of rectangle


# The Circle class is defined with an __init__ method
# that initializes a radius instance variable.
# It also defines an area method that calculates and
# returns the area of a circle using the radius instance variable.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Initialize radius instance variable

    def area(self):
        return 3.14 * self.radius**2  # Return area of circle using pi * r^2


shapes = [Rectangle(200, 200), Circle(1)]
for shape in shapes:
    print(shape.area())
