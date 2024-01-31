# BFS를 위해 deque 사용
from collections import deque

n, m = map(int, input().split())

# 지도를 입력
a = [list(map(int, input().split())) for _ in range(n)]
# 방문 여부 확인용 리스트
visited = [[0 for _ in range(m)] for _ in range(n)]

def bfs():
    while q:
        # 탐색 중인 위치
        r, c = q.popleft()

        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            # 인접한 칸 확인
            nr, nc = r + dr, c + dc

            # 격자 내부인지, 뱀은 없는지, 방문한 적이 없는지 등 확인
            if 0 <= nr < n and 0 <= nc < m and a[nr][nc] == 1 and not visited[nr][nc]:
                # 방문한 것으로 체크
                visited[nr][nc] = 1
                # 다음으로 탐색하기 위해 queue에 추가
                q.append((nr, nc))

q = deque()
# (0, 0)은 탐색 성공
visited[0][0] = 1
q.append((0, 0))

bfs()

print(visited[n - 1][m - 1])