"""
DECORATOR FOUNDATION CONCEPTS

Before learning decorators, understand these 4 ideas:

1. Functions have inputs and outputs.
2. Functions can be nested.
3. Functions are first-class objects (can be assigned to variables and passed as arguments).
4. Functions can be returned from other functions.

Decorators are built using all four concepts.
"""

# ==========================================================
# 1. FUNCTIONS HAVE INPUTS AND OUTPUTS
# ==========================================================

def add(a, b):
    """Takes two inputs and returns one output."""
    return a + b


result = add(2, 3)

print("1. Functions Have Inputs and Outputs")
print("Result:", result)
print()


# ==========================================================
# 2. FUNCTIONS CAN BE NESTED
# ==========================================================

def outer_function():
    """A function defined inside another function."""

    def inner_function():
        print("Hello from inner function")

    # Calling the nested function
    inner_function()


print("2. Nested Functions")
outer_function()
print()


# ==========================================================
# 3. FUNCTIONS ARE FIRST-CLASS OBJECTS
# ==========================================================

def greet():
    print("Hello")


# Store a function inside a variable
say_hello = greet

print("3A. Function Stored in Variable")
say_hello()
print()


# Pass a function as an argument
def run_function(function):
    """
    Receives a function as input and executes it.
    """
    function()


print("3B. Function Passed as Argument")
run_function(greet)
print()


# ==========================================================
# 4. FUNCTIONS CAN BE RETURNED
# ==========================================================

def outer():
    """
    Returns another function.
    """

    def inner():
        print("Hello from returned function")

    return inner


# outer() returns inner
returned_function = outer()

print("4. Function Returned From Another Function")
returned_function()
print()


# ==========================================================
# COMBINING EVERYTHING (DECORATOR FOUNDATION)
# ==========================================================

def decorator_function(original_function):
    """
    Receives a function as input.
    Creates a nested function.
    Returns the nested function.
    """

    def wrapper():
        print("Before original function")

        original_function()

        print("After original function")

    return wrapper


def display():
    print("Hello from display()")


# Pass display() into decorator_function
decorated_display = decorator_function(display)

print("5. Decorator Logic Without @ Symbol")
decorated_display()
print()


# ==========================================================
# ACTUAL DECORATOR SYNTAX
# ==========================================================

def logging_decorator(function):
    """
    This is a real decorator.
    """

    def wrapper():
        print("Before function execution")

        function()

        print("After function execution")

    return wrapper


@logging_decorator
def hello():
    print("Hello World")


print("6. Decorator Using @ Syntax")
hello()
print()


# ==========================================================
# DECORATOR WITH ARGUMENTS
# ==========================================================

def log_function(function):

    def wrapper(*args):
        print(f"Function Name: {function.__name__}")
        print(f"Arguments: {args}")

        result = function(*args)

        print(f"Returned Value: {result}")

        return result

    return wrapper


@log_function
def divide(a, b):
    return a / b


print("7. Decorator With Arguments")
divide(10, 2)

































print('fck up ueself')















# ==========================================================
# 1. FUNCTIONS HAVE INPUTS AND OUTPUTS
# ==========================================================

# Functions can take input parameters and return output values.

def add(a, b):
    return a + b

result = add(5, 3)

print(result)  # Output: 8


# ==========================================================
# 2. FUNCTIONS CAN BE NESTED
# ==========================================================

# A function can be defined inside another function.

def outer_function():

    def inner_function():
        print("Hello from inner function")

    inner_function()

outer_function()


# ==========================================================
# 3. FUNCTIONS ARE FIRST-CLASS OBJECTS
# ==========================================================

# Functions can be:
# - Stored in variables
# - Passed as arguments to other functions

def greet():
    print("Hello")


# Store function in a variable
say_hello = greet

say_hello()


# Pass function as an argument
def run_function(function):
    function()

run_function(greet)


# ==========================================================
# 4. FUNCTIONS CAN BE RETURNED FROM OTHER FUNCTIONS
# ==========================================================

# A function can create and return another function.

def outer():

    def inner():
        print("Hello from returned function")

    return inner


returned_function = outer()

returned_function()