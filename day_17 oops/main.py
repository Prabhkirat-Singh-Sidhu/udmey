#classes

class ussr:
    pass # just used to skip 


# PascalCase naming
# camelCase
# snake_case

# atributes: its a peice of data/variable which is associated with object


class User1:

    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0 
    
    def follow(self,user):
        user.followers += 1
        self.following += 1


      #method 2 
user_1 = User1("001", "angla")
user_2 = User1("002","jack")


user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.following)
print(user_2.followers)



# class user:
#     pass

# user_1 = user() #object


# #attribute 1
# user_1.id = "002" 
# user_1.username = "walla habibi" #second attribute


# user_2 = user() #object

# #attibute 2
# user_2.id = "00.2"
# user_2.username = "jack"