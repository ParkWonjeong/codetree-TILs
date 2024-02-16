answer = "No"

n = int(input())
value = (n // 10) + (n % 10)
if (n % 2 == 0) and (value % 5 == 0):
    answer = "Yes"

print(answer)