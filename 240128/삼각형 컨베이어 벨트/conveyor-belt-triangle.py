n, t = map(int, input().split())

arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
arr_3 = list(map(int, input().split()))

def turning():
    last_num_1 = arr_1[-1]
    last_num_2 = arr_2[-1]
    last_num_3 = arr_3[-1]

    # 첫 번째 벨트 이동
    for i in range(n - 1, 0, -1):
        arr_1[i] = arr_1[i - 1]
    # 세 번째 벨트에서 값 전달
    arr_1[0] = last_num_3

    # 두 번째 벨트 이동
    for j in range(n - 1, 0, -1):
        arr_2[j] = arr_2[j - 1]
    # 첫 번째 벨트에서 값 전달
    arr_2[0] = last_num_1

    # 세 번째 벨트 이동
    for k in range(n - 1, 0, -1):
        arr_3[k] = arr_3[k - 1]
    # 두 번째 벨트에서 값 전달
    arr_3[0] = last_num_2

for _ in range(t):
    turning()

for first_num in arr_1:
    print(first_num, end = " ")
print()
for second_num in arr_2:
    print(second_num, end = " ")
print()
for third_num in arr_3:
    print(third_num, end = " ")