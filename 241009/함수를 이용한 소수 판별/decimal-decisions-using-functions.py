a, b = list(map(int, input().split()))

def is_prime_number(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

total_value = 0

for i in range(a, b + 1):
    if is_prime_number(i):
        total_value += i

print(total_value)