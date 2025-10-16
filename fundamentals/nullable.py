from typing import Optional

# nulalble
print("Using int | None")
my_var: int | None = 10
print(my_var)

my_var = None
print(my_var)
print(my_var is None)
print(my_var is not None)

print("Using Optional[int]")
other: Optional[int] = 11
print(other)
other = None
print(other)
print(other is None)
