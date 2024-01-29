K, N = map(int, input().split())
answer = []
def numbers(curr_num):
    if curr_num == N:
        for elem in answer:
            print(elem, end = " ")
        print()
        return
    
    for i in range(1, K + 1):
        answer.append(i)
        numbers(curr_num + 1)
        answer.pop()
    return

numbers(0)