n = int(input())
BLANK = 0

arr = [int(input()) for _ in range(n)]
bomb_1 = list(map(int, input().split()))
bomb_2 = list(map(int, input().split()))

temp_1 = []
for i in range(bomb_1[0] - 1, bomb_1[1]):
    arr[i] = 0

for i in range(n):
    if arr[i] != BLANK:
        temp_1.append(arr[i])

arr = temp_1

for i in range(bomb_2[0] - 1, bomb_2[1]):
    arr[i] = 0

temp_2 = []
for i in range(len(arr)):
    if arr[i] != BLANK:
        temp_2.append(arr[i])

print(len(temp_2))

for elem in temp_2:
    print(elem)