def hello_if(number: int):
    if number == 0:
        print("Zero")
    elif number == 1:
        print("One")
    else:
        print("Another number: ", end=str(number))


hello_if(0)
hello_if(1)
hello_if(99)
