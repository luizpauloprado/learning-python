# Lists:
# Heterogeneous: Can store elements of different data types (e.g., integers, strings, other lists) within the same list.
# Dynamic Size: Can grow or shrink in size as elements are added or removed.
# Built-in: Lists are a fundamental, built-in data type in Python.
# Flexibility: Offer broad functionality for general-purpose data storage and manipulation.

# Arrays (from the array module or NumPy arrays):
# Homogeneous: Typically store elements of a single, specified data type (e.g., all integers, all floats).
# Fixed Size (for array module): Arrays created with the array module have a fixed size upon creation, although NumPy arrays can be more flexible.
# Specialized: Designed for efficient storage and manipulation of large collections of numerical data, especially in the context of scientific computing and data analysis (NumPy arrays are widely used for this).
# Memory Efficiency: Generally more memory-efficient than lists for storing large amounts of homogeneous data due to their optimized internal representation.

# list
numbers: list = [1, 2, 3]
alphabet: list[str] = ["a", "b", "c", "d"]
print(numbers)
print(numbers * 3)
print(alphabet)
print(alphabet[0:2])
print(alphabet[2:])
print(numbers + [4, 5])

# two types together
x = [numbers, alphabet]
print(x)

# methods
numbers.append(4)  # numbers.append([5, 6, 7]) = result [1, 2, 3, 4, [5, 6, 7]]
print(numbers)

numbers.insert(0, 99)
print(numbers)

numbers.remove(99)
print(numbers)

count1 = numbers.count(1)  # return number of occurrences of value
print(count1)

index = numbers.index(1)
print(index)
print(numbers[index])

numbers.extend([9, 8, 7])
print(numbers)

numbers.clear()

numbers = [1, 2, 3]
numbers.reverse()
print(numbers)

reverseAlphabet = reversed(alphabet)
print(list(reverseAlphabet))

# sort a list
unsorted = [1, 99, 98, 2]
print("sort asc")
print(sorted(unsorted))
print("sort desc")
print(sorted(unsorted, reverse=True))

# list comprehensions
plus1 = [x + 1 for x in numbers]
print(numbers)
print("plus 1")
print(plus1)

upper = [item.upper() for item in alphabet]
print(alphabet)
print("upper")
print(upper)
