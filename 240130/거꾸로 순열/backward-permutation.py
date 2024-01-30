n = int(input())

visited = [0 for _ in range(n + 1)]
answer = []

def print_answer():
    for elem in answer:
        print(elem, end = " ")
    print()

def choose(curr_num):
    if curr_num == n + 1:
        print_answer()
        return
    
    for i in range(n, 0, -1):
        if visited[i] == 1:
            continue
        
        visited[i] = 1
        answer.append(i)

        choose(curr_num + 1)

        answer.pop()
        visited[i] = 0

choose(1)