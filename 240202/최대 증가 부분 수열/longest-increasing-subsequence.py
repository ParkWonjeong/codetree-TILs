n = int(input())
arr = list(map(int, input().split()))

increasing_arr_cnt = []

for i in range(n):
    increasing_arr = []
    increasing_arr.append(arr[i])

    for j in range(i + 1, n):
        if arr[j] > increasing_arr[-1]:
            increasing_arr.append(arr[j])
    
    increasing_arr_cnt.append(len(increasing_arr))
    
print(max(increasing_arr_cnt))