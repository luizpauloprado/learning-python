# set
basket: set[str] = {"apple", "orange", "banana"}
print(basket)

# no duplicated
basket_with_duplicated: set[str] = {
    "apple",
    "orange",
    "apple",
    "pear",
    "orange",
    "banana",
}
print(basket_with_duplicated)  # show that duplicates have been removed

# has / in
print("banana" in basket)
print("pear" in basket)

# Demonstrate set operations on unique letters from two words
a = set("abracadabra")
b = set("alacazam")
print("unique letters abracadabra")
print(a)
print("unique letters alacazam")
print(b)
print("letters in a but not in b")
print(a - b)
print("letters in a or b or both")
print(a | b)
print("letters in both a and b")
print(a & b)
print("letters in a or b but not bot")
print(a ^ b)
