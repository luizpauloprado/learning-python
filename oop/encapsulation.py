# _protected_var
# The _protected_var is marked as protected by using a single underscore prefix.
# This means that the attribute can be accessed within the class and its subclasses but not outside the class


# __private_var
# The __private_var is marked as private by using two underscore prefixes.
# This means that the attribute can only be accessed within the class and not outside the class, not even in its subclasses.
class MyClass:
    kind = "canine"  # class variable shared by all instances

    def __init__(self, name: str):
        self._protected_var = 10
        self.__private_var = 20
        self.name = name

    def hello(self):
        print("Hello Class!")


obj = MyClass(name="Luiz")
print("Protected var:")
print(obj._protected_var)
print("Just a var:")
print(obj.name)
print("Call hello method:")
obj.hello()
print("Private var - throws an error:")
print(obj.__private_var)
