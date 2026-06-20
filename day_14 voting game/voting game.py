#follower game

from game_data import data

import random

def format_data(acc):

    acc_name = acc["name"]
    acc_dec = acc["description"]
    acc_conti = acc["country"]
    return(f"{acc_name}, a {acc_dec}, from {acc_conti}")

def check_no(user_guess, a_follow, b_follow):
    if a_follow > b_follow:
        return user_guess == "a"
    else:
        return user_guess == "b"
    

    
loop = True
score = 0
acc_b = random.choice(data)


while loop:
    acc_a = acc_b
    acc_b = random.choice(data)

    if acc_a == acc_b:
        acc_b = random.choice(data)

    print(f"Compare A:{format_data(acc_a)}")
    print("VS")
    print(f"Compare A:{format_data(acc_b)}")

    guess = input("Who has more follower ? Type A or B").lower()

    a_follower_count = acc_a["follower_count"]
    b_follower_count = acc_b["follower_count"]


    is_correct = check_no(guess, a_follower_count, b_follower_count)

    if is_correct:
        score +=1
        print(f" thats right{score}")
    else:
        print(f"soory thats wrong{score}")
        loop = False