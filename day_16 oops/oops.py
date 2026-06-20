#
'''
    attributes = data/ variable
    method = function

class: blueprint
    

object: result 
    
'''

from turtle import Turtle, Screen
obj = Turtle()
print(obj)
obj.shape('turtle')

x= int(input("enter the value\n"))
if x ==1:
    my_screen = Screen()
    print(my_screen.canvheight)
elif x>1:
    obj.forward(100)
    obj.left(90)
    obj.right(456)
    
my_screen.exitonclick()