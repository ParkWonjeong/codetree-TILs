a, b = map(int, input().split())

cnt = 0

def three_six_nine(i):
    if i % 3 == 0:
        return True
    while i > 0:
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            return True
        i = i // 10

for i in range(a, b + 1):
    if three_six_nine(i):
        cnt += 1

print(cnt)