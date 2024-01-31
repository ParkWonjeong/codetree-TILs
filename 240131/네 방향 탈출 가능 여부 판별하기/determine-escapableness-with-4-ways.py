from collections import deque
n, m = map(int, input().split())

# 지도 입력
a = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)] # 각 정점의 방문 여부를 확인하는 리스트

def bfs():
    # q를 가지고 너비 우선 탐색
    while q:
        r, c = q.popleft() # 현재 위치가 r행 c열을 탐색 중이다.
        
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + dr, c + dc # r, c와 인접한 칸인 (nr, nc) 찾기

               # 격자를 벗어나지 않는지          / 해당 위치에 뱀이 없는지 / 방문한 적 없는지 
            if 0 <= nr < n and 0 <= nc < n and a[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))

q = deque() # 새로운 queue를 생성
visited[0][0] = 1 # (0, 0)은 탐색 성공

q.append((0, 0))

bfs() # 탐색 수행

print(visited[n - 1][m - 1])