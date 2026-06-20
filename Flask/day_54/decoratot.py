# import time

# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         #do somthing before 

        
#         function()
#         time.sleep(5)
#         function()
#         #do somthing after

# @delay_decorator
# def say_hellow():
#     print("hellow")

# say_hellow()






import time

def delay_decorator(function): #delay_decorator(say_hello)

    def wrapper_function():
        time.sleep(2)

        # Before function
        print("Before function")

        function()

        time.sleep(5)

        function()

        # After function
        print("After function")

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


say_hello()

# @ work as same which is at below
decorated_fnc = delay_decorator(say_hello) # give ->wrapper_function<- at the end
decorated_fnc() # call the wrapper_function()





# ## py decorator

# def dec_fnc(fnc):


#     def wrapper_fnc():
#         fnc()


#     return wrapper_fnc

# dec_fnc()