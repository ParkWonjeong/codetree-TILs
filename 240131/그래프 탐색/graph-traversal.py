N, M = tuple(map(int, input().split()))
graph = [
    []
    for _ in range(N + 1)
]
visited = [False for _ in range(N + 1)]
vertex_cnt = 0

# dfs 함수 정의
def dfs(vertex):
    # 전역 변수로 호출
    global vertex_cnt

    # 재귀적으로 탐색 및 카운트
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            vertex_cnt += 1
            dfs(curr_v)

# 입력 받은 후 인접 행렬에 추가
for i in range(M):
    v1, v2 = tuple(map(int, input().split()))

    graph[v1].append(v2)
    graph[v2].append(v1)

visited[1] = True
dfs(1)

print(vertex_cnt)