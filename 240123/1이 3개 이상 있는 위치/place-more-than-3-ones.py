n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

answer = 0

def adjacent_cnt(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1

    return cnt

for i in range(n):
    for j in range(n):
        if adjacent_cnt(i, j) >= 3:
            answer += 1

print(answer)