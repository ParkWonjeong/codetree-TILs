n, t = map(int, input().split())

belt_1 = list(map(int, input().split()))
belt_2 = list(map(int, input().split()))

while t > 0:
    temp_1 = belt_1[n - 1]
    temp_2 = belt_2[n - 1]
    for i in range(n - 1, 0, -1):
        belt_1[i] = belt_1[i - 1]
    for i in range(n - 1, 0, -1):
        belt_2[i] = belt_2[i - 1]
    belt_1[0] = temp_2
    belt_2[0] = temp_1
    t -= 1

for elem in belt_1:
    print(elem, end = " ")
print()
for elem in belt_2:
    print(elem, end = " ")