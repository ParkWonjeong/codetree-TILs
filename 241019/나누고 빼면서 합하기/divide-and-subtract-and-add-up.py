n, m = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

def div_sub_func(m):
    answer = 0
    while m != 1:
        if m % 2 == 0:
            answer += arr[m - 1]
            m //= 2
        else:
            answer += arr[m - 1]
            m -= 1
    answer += arr[0]
    return answer

print(div_sub_func(m))