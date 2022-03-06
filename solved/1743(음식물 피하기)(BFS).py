## 백준 1743 음식물 피하기
import sys
input = sys.stdin.readline
from collections import deque

# 1. 세로 n, 가로 m 크기의 이중 리스트를 만든다.(.로 만들기)
# 2. 입력받은 좌표에 따라 해당 행열에 #을 넣는다.(#은 음식물)
# 3. 인접 행열 방식으로 그룹마다 음식물 크기 구해서 최종적으로 제일 큰 max를 구한다.
# 4. BFS

def BFS(x, y):
    global cnt

    queue = deque()
    queue.append([x, y])
    cnt += 1
    visited[x][y] = 1

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            xx = a + dx[i]
            yy = b + dy[i]
            if 0 <= xx < n and 0 <= yy < m and visited[xx][yy] == 0 and graph[xx][yy] == '#':
                queue.append([xx, yy])
                cnt += 1
                visited[xx][yy] = 1


n, m, k = map(int, input().split())

graph = [['.']*m for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = '#'

# 방향 (좌우상하)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[0]*m for _ in range(n)]
cnt_list = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == '#' and visited[i][j] == 0:
            cnt = 0
            BFS(i, j)
            cnt_list.append(cnt)

print(max(cnt_list))
