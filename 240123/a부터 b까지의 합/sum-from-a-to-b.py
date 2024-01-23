a, b = input().split()
a, b = int(a), int(b)

sum_value = 0
for i in range(a, b + 1):
    sum_value += i

print(sum_value)