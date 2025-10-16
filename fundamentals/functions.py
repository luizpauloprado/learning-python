def hello_lp():
    return "Hello LP!"


def hello(name):
    return f"Hello {name}!"


# default argument values
def hello_with_age(name, age: int = 1):
    return f"{name} age is {age}"


def my_list(l=[]):
    print(l)


print(hello_lp())
print(hello(name="Luiz"))
print(hello_with_age("LP", 37))
print(hello_with_age(name="LP", age=37)) # keyword arguments
print(hello_with_age(name="LP"))
print(hello_with_age(age=99, name="Luli"))

my_list([1])
my_list([21, 22, 23])
my_list()
