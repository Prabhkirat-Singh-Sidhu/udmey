def calculate_love_score(name1,name2):
    true_= 0
    love= 0
    for letter in name1 + name2:
        letter=letter.lower()
        if letter == "t" or letter == "r" or letter == "u" or letter == "e":
            true_+= 1
        
    for letter in name2 + name1:
        letter=letter.lower()
        if letter == "l" or letter == "o" or letter == "v" or letter == "e":
            love += 1 
    print(f"{true_}{love}")


calculate_love_score("Kanye West", "Kim Kardashian")



#alternate
def calculate_love_score(name1, name2):
    true_ = 0
    love = 0

    for letter in (name1 + name2).lower():
        if letter in "true":
            true_ += 1
        if letter in "love":
            love += 1

    print(f"{true_}{love}")


#alternate2
