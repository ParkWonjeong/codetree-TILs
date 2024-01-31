N, M = tuple(map(int, input().split()))

#index를 1번 부터 사용하기 위해 m+1만큼 할당합니다.
graph = [[] for _ in range(N + 1)]

visited = [False for _ in range(N + 1)]
vertex_cnt = 0


def dfs(vertex):
    global vertex_cnt
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            vertex_cnt += 1
            dfs(curr_v)
    
    
for i in range(M):
    v1, v2 = tuple(map(int, input().split()))
    graph[v1].append(v2)
    graph[v2].append(v1)

visited[1] = True
dfs(1)

print(vertex_cnt)