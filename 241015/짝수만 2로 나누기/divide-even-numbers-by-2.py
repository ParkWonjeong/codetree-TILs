n = int(input())

arr = list(map(int, input().split()))

def divide_if_even(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2

divide_if_even(arr)
for elem in arr:
    print(elem, end = " ")