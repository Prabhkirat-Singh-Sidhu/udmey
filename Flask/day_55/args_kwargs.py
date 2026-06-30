'''*args and **kwargs allow a function to accept a variable number of arguments.

*args → collects extra positional arguments into a tuple.
**kwargs → collects extra keyword arguments into a dictionary.'''

def add(a, b):
    print(a + b)

add(2, 3)

#The function expects exactly 2 arguments.

#if you do add(2,3,4)   that will give error

# that where args come in
def add(*args):
    print(args)

add(1, 2, 3, 4, 5)


#example

def add(*args):
    total = 0

    for i in args:
        total += i
        total1 = i + total1

add(1,2,3,4)



#for kwargs
def person(**kwargs):
    print(kwargs)

person(name="John", age=20)