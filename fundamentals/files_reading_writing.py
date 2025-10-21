import csv

print(".txt:")
with open("sample.txt", "r") as file:
    txt_content = file.read()

print(txt_content)

with open("sample.txt", "r") as file:
    txt_content_lines = file.readlines()

print(txt_content_lines)

with open("sample.txt", "r") as file:
    for line in file:
        print(line, end="")

# with open("sample.txt", "a") as file:
#     file.write("Vai dar tudo certo <3")

print(".csv:")

with open("sample.csv", "r") as file:
    for line in file:
        print(line.split(","))

with open("sample.csv", "r") as file:
    csv_content = csv.reader(file, delimiter=",")
    for line in csv_content:
        print(line)

with open("sample.csv", "r") as file:
    csv_content = csv.DictReader(file)
    for line in csv_content:
        print(line)
