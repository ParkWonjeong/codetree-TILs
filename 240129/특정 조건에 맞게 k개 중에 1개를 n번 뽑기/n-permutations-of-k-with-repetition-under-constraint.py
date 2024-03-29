K, N = map(int, input().split())
answer = []

def print_answer():
    for elem in answer:
        print(elem, end = " ")
    print()


def choose_num(cnt):
    if cnt == N:
        print_answer()
        return

    for i in range(1, K + 1):
        if cnt >= 2 and answer[-1] ==i and answer[-2] == i:
            continue
        answer.append(i)
        choose_num(cnt + 1)
        answer.pop()
    return

choose_num(0)