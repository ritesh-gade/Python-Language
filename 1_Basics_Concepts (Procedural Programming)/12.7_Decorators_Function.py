# Decorators:- 1) A decorator is a function that takes another function as an argument and return a new function that modifies the behavior of the original function. 
#              2) Decorator are powerful and versatile tool that allow you to modify the behavior of function and methods. 
#              3) They are a way to extend the functionality of a function or method without modifying its source code . 

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello World !!!")

@greet
def add(a, b):
    print(a+b)

# greet(hello)()   # same as the line no 21
hello()

# greet(add)(2,3)   # same as the line no 24
add(2,3)
