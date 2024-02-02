n = int(input())

memo = [-1] * (n + 1)
def fibbo(n):
    if memo[n] != -1:
        return memo[n]

    if memo[n] <= 2:
        memo[n] = 1
    else:
        memo[n] = fibbo(n - 1) + fibbo(n - 2)

    return memo[n]

answer = fibbo(n)

print(answer)