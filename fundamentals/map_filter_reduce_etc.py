from functools import reduce

# map, filter, and reduce are higher-order functions in Python
# that facilitate functional programming paradigms
# They operate on iterables, such as lists, and are often used with lambda functions for concise code

numbers: list[int] = [2, 4, 6]
squared = map(lambda number: number * 2, numbers)
print("map")
print(numbers)
print(list(squared))

filtered = filter(lambda number: number != 6, numbers)
print("filter")
print(numbers)
print(list(filtered))

reduced = reduce(lambda acc, val: acc + val, numbers)
print("reduce")
print(numbers)
print(reduced)

print("sum")
print(numbers)
print(sum(numbers))

print("min")
print(numbers)
print(min(numbers))

print("max")
print(numbers)
print(max(numbers))

print("next")
print(numbers)
print(next(iter(numbers)))
print(numbers)

# any() and all(): Check if any or all elements of an iterable are true
booleans = [True, True, False]
print("any (true)")
print(any(booleans))

print("all (true)")
print(all(booleans))
