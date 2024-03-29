from collections import deque
n, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

q = deque()

cnt = 0

def bfs():
    while q:
        x, y = q.popleft()
        visited[x][y] = 1

        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if can_go(new_x, new_y):
                q.append((new_x, new_y))
                visited[new_x][new_y] = 1
                

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and not grid[x][y]

for _ in range(k):
    x, y = tuple(map(int, input().split()))
    q.append((x - 1, y - 1))

bfs()

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:
            cnt += 1

print(cnt)