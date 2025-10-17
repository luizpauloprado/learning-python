def decorator_func(func):
    def wrapper():
        print("start")
        func()
        print("end")

    return wrapper


@decorator_func
def foo():
    print("Hello world!")


foo()
