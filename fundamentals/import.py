import import_sample  # Importing a file in the same directory
from import_specific import greet, MyClass  # Importing specific items from a file
from import_all import *
import import_all as my_all

print(import_sample.hello())
print(greet("Lulu"))
print(MyClass)
func_a()
func_b()
my_all.func_a()
my_all.func_b()
