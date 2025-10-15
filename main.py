def hello():
    print("Hello LP!")


def hello_if(number: int):
    if number == 0:
        print("Zero")
    elif number == 1:
        print("One")
    else:
        print("Another number: ", end=str(number))


print("Hello World!")
hello()
hello_if(51)
