def make_a_plus(value=0):
    return lambda x: x + value


plus_1 = make_a_plus()
print(plus_1(1))

plus_10 = make_a_plus()
print(plus_10(10))

add = lambda x, y: x + y
print(add(1, 1))

greeting = lambda name: print(f"Hello {name}")
greeting("LP")
