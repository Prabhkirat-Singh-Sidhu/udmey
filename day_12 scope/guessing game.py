import random

no = random.randint(0,100)

life = 0

dif = input("e for Easy, d for difficult:")



loop = True

def check_no(user):

    global loop 

    if no > user:
        print('Too Low')
        
    elif no < user:
        print("Too High")
        
    elif no == user:
        print("\n"*20)
        print("Correct u Win")
        loop = False
        return loop
    else:
        print("Enter valid input")

while loop:
    if dif == 'e':
        life = 10
        for i in range (life):
            user = int(input('Enter the value: ')) 
            check_no(user)
            print(f"Life left are: {life - i - 1}")
        if loop == True:
            print("u lose")
            loop = False    
    
    elif dif == "d":
        life = 5
        for i in range (life): 
            user = int(input('Enter the value: '))
            check_no(user)
            
            print(f"Life left are: {life - i - 1}")
        
        if loop == True:
            print("u lose")
            loop = False   