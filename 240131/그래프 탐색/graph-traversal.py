N, M = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(M)]
cnt = 0

for elem in arr:
    if 1 in elem:
        cnt += 1

print(cnt)