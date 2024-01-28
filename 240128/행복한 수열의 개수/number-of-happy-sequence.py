n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

seq = [0 for _ in range(n)]

def is_happy_sequence():
    happy_num, max_val = 1, 1
    for i in range(1, n):
        if seq[i - 1] == seq[i]:
            happy_num += 1
        else:
            happy_num = 1

        max_val = max(max_val, happy_num)
    return max_val >= m

num_happy = 0

for i in range(n):
    seq = grid[i][:]

    if is_happy_sequence():
        num_happy += 1

for j in range(n):
    for i in range(n):
        seq[i] = grid[i][j]

    if is_happy_sequence():
        num_happy += 1

print(num_happy)