def add_number(a, b):
    return a + b

def subtraction_number(a, b):
    return a - b

def divide_number(a, b):
    return a // b

def multiple_number(a, b):
    return a * b

a, symbol, b = list(input().split())
a = int(a)
b = int(b)

if symbol == "+":
    print(a, symbol, b, "=", add_number(a, b))
elif symbol == "-":
    print(a, symbol, b, "=", subtraction_number(a, b))
elif symbol == "/":
    print(a, symbol, b, "=", divide_number(a, b))
elif symbol == "*":
    print(a, symbol, b, "=", multiple_number(a, b))
else:
    False