n, m, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
pieces = [1 for _ in range(k)]

ans = 0

def score_calc():
    score = 0
    for piece in pieces:
        score += (piece >= m)

    return score

def find_max(cnt):
    global ans
    ans = max(ans, score_calc())

    if cnt == n:
        return
    
    for i in range(k):
        if pieces[i] >= m:
            continue

        pieces[i] += arr[cnt]
        find_max(cnt + 1)
        pieces[i] -= arr[cnt]

find_max(0)
print(ans)