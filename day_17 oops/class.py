class User:
    pass
user_1 = User() #object



#creating/passsing the value of attribute directly using object name

user_1.username = "JATT MAULLA" #variable that is associated with the object or can say attached with object can call them using object 
user_1.id = "001"



#calling attribute of an object
print(user_1.id)




#constructor (used to initlize the blueprint)
'''
use __init__ and self:-
the initilization is done to an object when its is constructed 
i.e. it means that when u create a object it decide what will initilize for eg if i am making a building the iron structre should be initilized 
syntax:
def __init__(self):



what is self:-
actual object that is being pass down to the function

without it we have to manually add the object into the function which cant be possible..



'''

class Student:

    def __init__(self, name):
        self.name = name

s1 = Student("Sidhu")
s2 = Student("Aman")
print(s1)
'''

for s1:
s1 = student("sidhu")

Python roughly does:
Student.__init__(s1, "Sidhu")

and become:
__init__(s1, "Sidhu")




Read It In English
self.name = name

means:

Create/store an attribute called name inside this object, and put the value from the parameter name into it.

'''

