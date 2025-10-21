pokemons = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu"]

print("first, *rest=")
first, *rest = pokemons
print(first)
print(rest)

print("first, second, *rest=")
first, second, *rest = pokemons
print(first)
print(second)
print(rest)

print("first, *middle, rest=")
first, *middle, last = pokemons
print(first)
print(middle)
print(last)

print("like spread=")
a, *rest_items = pokemons
result = rest_items + ["Dittinho"]
print(rest_items + ["Ditto"])
print(result)
