#multi return value

def fn1(text):
    return text + text

def fn2(text):
    return text.title()

text = "prabh"

yo = fn1(text)
print(yo)

xo = fn2(yo )
print(xo)


