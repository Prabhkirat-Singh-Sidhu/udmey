#modifying global scope

enime = 0

def increases_enime():
    global enime
    enime +=1

def inc_eni(eny):
    return eny + 1

enime = inc_eni(enime) # it will change the value without changing the global scope inside function


#global constant syntax:'all upper case'

PI = 3.14


