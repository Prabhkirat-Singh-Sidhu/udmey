# TODO: Create the logging_decorator() function 👇

def logging_decorator(fnc):
    def wrapper(*args):
        print(f"You called {fnc.__name__}{args}")
        result = fnc(*args)
        print(f"It returned: {result}")
        return result
    return wrapper

# TODO: Use the decorator 👇

def a_function(*args):
    return sum(args)
a_function = logging_decorator(a_function)

a_function(4,5,6)


'''
 args for packing into tuples
*args used for unpacking and creating seprate values for each.
'''

# def a_function(*args): 
#     print(f"this is args var: { args}")
#     return sum(args)

# print(a_function(4,5,6))
