y = int(input())

def leap_year(i):
    if i % 4 == 0:
        if i % 100 == 0 and i % 400 != 0:
            return "false"
        return "true"

print(leap_year(y))