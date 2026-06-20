#functions
def greet_with(name, last_name):
    if name == "prabh" and last_name == "sidhu":
        print("Hello Prabh Sidhu nice to meet you!")
    else:
        print('gairo se baat nhi karte')

greet_with("prabh","sidhu")#positional parameter
greet_with(last_name="sandhu",name="navan")#keyword argument


# name = 'prabh'
# last_name = 'sidhu'
# greet_with()