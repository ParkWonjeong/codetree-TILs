a, b = map(int, input().split())

def prime_number(i):
    divisor = 0
    for j in range(1, i + 1):
        if i % j == 0:
            divisor += 1
    if divisor == 2:
        return True
    else:
        return False

def odd_style_number(i):
    hundreds_number = i // 100
    tens_number = i // 10
    units_number = i % 10

    added_value = hundreds_number + tens_number + units_number
    if added_value % 2 == 0:
        return True
    else:
        return False

prime_and_odd_numbers = 0

for i in range(a, b + 1):
    if prime_number(i):
        if odd_style_number(i):
            prime_and_odd_numbers += 1
    
print(prime_and_odd_numbers)