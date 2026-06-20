def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

operation= {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

sym= input("Enter the u want to use + - * /\n")


n1= int(input("enter First dighit:"))
n2 = int(input("enter sec dighit:"))


ans = operation[sym](n1,n2)
print(ans)
conti = True

while True:

    hh=input("user want to continue type x to continue or any key to break:")

    if hh == "x":
        conti = True
        n1 = ans
        sym= input("Enter the u want to use + - * /\n")
        n2 = int(input("enter the amt for 2nd digit"))
        ans = operation[sym](n1,n2)
        print(ans)
    else:
        conti= False
        break
