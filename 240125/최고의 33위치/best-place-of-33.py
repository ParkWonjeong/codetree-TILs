n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def get_coin_num(row_s, row_e, col_s, col_e):
    coin_num = 0

    for row in range(row_s, row_e + 1):
        for col in range(col_s, col_e + 1):
            coin_num += arr[row][col]

    return coin_num

max_coin = 0

for row in range(n):
    for col in range(n):
        if (row + 2 >= n) or (col + 2 >= n):
            continue
        
        coin_num = get_coin_num(row, row + 2, col, col + 2)
        max_coin = max(coin_num, max_coin)

print(max_coin)