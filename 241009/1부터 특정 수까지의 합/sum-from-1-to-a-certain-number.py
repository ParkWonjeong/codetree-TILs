n = int(input())

def divide_total(n):
    total_value = 0
    for i in range(n + 1):
        total_value += i

    return total_value // 10

print(divide_total(n))