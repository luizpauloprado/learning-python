from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)
print(Color.RED.value)
print(Color["BLUE"])

for color in Color:
    print(color)
