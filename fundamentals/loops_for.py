# loops

# for
words: list[str] = ["cat", "window", "feet"]

for word in words:
    print(word, len(word))

for i in range(len(words)):
    print(i, words[i])

# enumerate
for index, value in enumerate(words):
    print(index, value)

# zip
questions = ["name", "age"]
answers = ["Luiz Paulo", "37"]
for question, answer in zip(questions, answers):
    print(f"What is your {question}? It is {answer}")

# reverse
for i in reversed(range(0, 6)):
    print(i)

# sorted
basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
print(basket)
for i in sorted(basket):
    print(i)

# sorted + set (unique elements)
print(set(basket))
for i in sorted(set(basket)):
    print(i)

# dictionary for
users: dict[str, str] = {"Luiz": "active", "Paulo": "inactive", "Mauricio": "inactive"}

for user, status in users.items():
    if status == "active":
        print("active user: " + user)
    else:
        print("inactive user: " + user)
