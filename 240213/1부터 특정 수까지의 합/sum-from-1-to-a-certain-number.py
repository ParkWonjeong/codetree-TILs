answer = 0
def sum_val(n):
    global answer
    for i in range(n + 1):
        answer += i
        
n = int(input())
sum_val(n)
print(answer // 10)