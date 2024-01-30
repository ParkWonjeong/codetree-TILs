k, n = map(int, input().split())
answer = []

def print_answer():
    for elem in answer:
        print(elem, end = " ")
    print()

def choosing():
    if len(answer) == 2:
        print_answer()
        return

    for i in range(1, k + 1):
        answer.append(i)
        choosing()
        answer.pop()
    return

choosing()