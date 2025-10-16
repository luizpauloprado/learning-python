# strings
sample: str = "yes"
print(sample * 5)

text = "Put several " "strings" " to join"
print(text)

# raw strings
print(r"C:\some\name")

# character in position or slice
word: str = "Python"
print(word[0])
print(word[-1])  # last character
print(word[0:2])  # characters from position 0 (included) to 2 (exclude
print(word[:2])  # character from the beginning to position 2 (excluded)
print(word[4:])  # characters from position 4 (included) to the end
print(word[:2] + word[2:])  # from 0 to 2(excluded) + from 2(included) to the end
print(len(word))  # length

# case manipulation
print(word.lower())
print(word.upper())
print(sample.capitalize())

movie: str = "Viva a vida é uma festa"
print(movie)
print(movie.title())
print(movie.swapcase())

# embedding expressions
pi: float = 3.14
print(f"The value of pi is: {pi}")

# searching and replacing
tv_show: str = "Vale Tudo"
print(tv_show.find("Vale"))

sub_string: str = "Tudo"
if tv_show.find(sub_string) != -1:
    print(f'"{tv_show}" contains "{sub_string}" at index {tv_show.find(sub_string)}')
else:
    print(f'"{tv_show}" does not contain "{sub_string}"')

print(tv_show.count("Vale"))
print(tv_show.replace("Vale", "VALE"))

# formating and alignement
lulu: str = "  Lulu  "
print(lulu)
print(lulu.strip())
print(lulu.lstrip())
print(lulu.rstrip())

# spint and join
splited: list = tv_show.split()
print(splited)
print("".join(splited))

# checking properties
print("Luiz".isalnum())
print("Luiz".isalpha())
print("tv_show".isalpha())
print("luiz".islower())
print("Luiz".startswith("Lu"))
print("Luiz".endswith("Lu"))
