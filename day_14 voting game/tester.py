def check_number(user_guess, a):
    return user_guess == a


secret_number = 5
guess = int(input("Enter your guess: "))

result = check_number(guess, secret_number)

print(result)