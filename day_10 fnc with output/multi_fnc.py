#multi return value

def fn1(text):
    return text + text

def fn2(text):
    return text.title()

text = "prabh"

print(fn2(fn1(text)))
