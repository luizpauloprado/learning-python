# dict
tel: dict[str, str] = {"Luiz": "98117", "Lucas": "99754", "Giovana": "12345"}
print(tel)

# add
tel["Flávia"] = "45678"
print(tel)

tel.setdefault("José", "0000")
# setdefault(key, default): Returns the value of the specified key
# If the key does not exist, it inserts the key with the specified default value and returns that value

# update
tel["Flávia"] = "1111"
print(tel)

# update(iterable): Updates the dictionary with elements from another dictionary
# or an iterable of key-value pairs. Existing keys are overwritten, and new keys are added
tel.update({"José": "0001"})
print(tel)

# delete
flavia_tel_value = tel.pop("Flávia")
print("pop Flávia")
print(flavia_tel_value)
print(tel)

del tel["Lucas"]
print("del Lucas")
print(tel)

# get
luiz_tel = tel.get("Luiz")
print("get Luiz")
print(luiz_tel)

# has / in
print("Luiz" in tel)
print("Luizzzz" in tel)
print("Luizzzz" not in tel)

# list items
print(tel.items())

# list key and values
print(tel.keys())
print(tel.values())

# for usage
for key, value in tel.items():
    print(f"{key} number is: {value}")

# dict() constructor builds dictionaries directly from sequences of key-value pairs
ages = dict([("Luiz", 37), ("Paulo", 37)])
print(ages)

# sort
print("sort")
print(tel)
print(sorted(tel.items()))
print(sorted(tel.items(), reverse=True))
print("sort by number")
print(sorted(tel.items(), key=lambda t: t[1]))
