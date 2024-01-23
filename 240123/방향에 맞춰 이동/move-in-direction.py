N = int(input())
x, y = 0, 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
ESWN = ["E", "S", "W", "N"]
for _ in range(N):
    dir_str, dir_num = input().split()
    dir_num = int(dir_num)
    x, y = x + dx[ESWN.index(dir_str)] * dir_num, y + dy[ESWN.index(dir_str)] * dir_num

print(x, y)