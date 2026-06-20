class Dog:

    def __init__(self, name): 
        self.name = name # read as -> self.name is assigned as name i.e if name is actually tommy then according to obj d1 it become d1.name that assigned as tommy

    def bark(self):
        print(f"{self.name} says Woof!")

d1 = Dog("Tommy") #secerectly pass the self as d1
d2 = Dog("Rocky")

d1.bark() # secereactly pass the self value as d1
d2.bark()