
def logger(func):
    def warpper():
        print("Function is being called")
        return func()
    return warpper

@logger
def say_hello():
    print("Hello Noor ul huda")

say_hello()    