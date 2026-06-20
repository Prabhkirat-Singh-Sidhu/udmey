#scope 

enimes = 1

def increase_enimes():
    enimes = 2
    print(f"enimes inside fnc:{enimes}")

increase_enimes()

print(f"enimes outside fnc:{enimes}")

#local scope within the fnc
def drink_portion():
    potion_strength = 2 #local scope
    print(potion_strength)

drink_portion()

#global scope

player_health = 10 
print(player_health)

#also know as namespace scope.

# do python have block scope? 
"""
✅ Definition

Block scope means:

A variable created inside a block { } (like inside if, for, while) exists only inside that block.

Languages like C, Java, JavaScript (let/const) have block scope.

🚫 Does Python have block scope?

👉 NO. Python does NOT have block scope.
Python has:

Function scope

Module (global) scope

Class scope

But NOT block scope.

🔎 Example
if True:
    x = 10

print(x)


Output:

10


Why?

Because x is still accessible outside the if block.

In C/Java this would give an error."""