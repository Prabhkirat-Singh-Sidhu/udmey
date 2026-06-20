# error handling

try: 
    age = int(input("How old are u?"))

except ValueError:
    print('Type a INT format like 15,12')
    age = int(input("How old are u?"))
    
if age > 18:
    print("u can drive")
    