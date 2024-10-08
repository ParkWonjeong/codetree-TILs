n, m = map(int, input().split())

def least_common_multiple(n, m):
    arr_n = []
    arr_m = []
    
    for i in range(1, n+1):
        arr_n.append(i * m)

    for i in range(1, m+1):
        arr_m.append(i * n)

    for elem_n in arr_n:
        for elem_m in arr_m:
            if elem_n == elem_m:
                print(elem_n)
                return

least_common_multiple(n, m)