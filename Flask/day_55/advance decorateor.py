# def createa(user):
#     print("testing")

# createa(new_user)


class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False

#decorator
def is_authenticated(fun):

    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            fun(args[0])

    return wrapper

        
#@is_authenticated

def create(user):
    print(f"FUCK this decorator {user.name}")

create = is_authenticated(create)


new_user = User("wallahabibi")
new_user.is_logged_in = True

create(new_user)



'''new_user is an object created and have 2 attribute name and bollean value fro logged
....
that means the fnc gets the object as the parameter?? then when it called and user = new_user = wallahabibi??

'''


