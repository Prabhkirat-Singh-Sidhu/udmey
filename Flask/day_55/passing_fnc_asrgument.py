# def greet():
#     print("Hello")


# def execute(func):
#     print(func)


# execute(greet)




# # passing class as argument

# class User:

#     def __init__(self, name):
#         self.name = name


# def create_person(cls):
#     person = cls("Prabh")

#     return person


# user = create_person(User)

# print(user.name)




def greet():
    print("Hello")

def run(func):
    print(func)
    func()  #to call a function inside a function, via passing a func as special variable, as parameter for other fnc.

run(greet)