N, M = tuple(map(int, input().split()))
answer = []

def print_answer():
    for i in range(N):
        if answer[i] == 1:
            print(i + 1, end = " ")
    print()

def choose(curr_num, cnt):
    if curr_num == N + 1:
        if cnt == M:
            print_answer()
        return

    answer.append(1)
    choose(curr_num + 1, cnt + 1)
    answer.pop()

    answer.append(0)
    choose(curr_num + 1, cnt)
    answer.pop()

    return

choose(1, 0)