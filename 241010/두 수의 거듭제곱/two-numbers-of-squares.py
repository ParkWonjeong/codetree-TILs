a, b = list(map(int, input().split()))

def multiple(a, b):
    value = 1
    for _ in range(b):
        value *= a

    return value

print(multiple(a, b))