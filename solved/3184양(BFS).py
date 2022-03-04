## 백준 3184 양
# BFS

import sys
input = sys.stdin.readline
from collections import deque

# BFS
def BFS(x, y):
    global o, v
    visited[x][y] = 1
    queue = deque()
    queue.append([x, y])
    oo = 0  # 한 울타리 내 양의 수
    vv = 0  # 한 울타리 내 늑대의 수
    if graph[x][y] == 'o': oo += 1
    elif graph[x][y] == 'v': vv += 1
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            xx = a + dx[i]
            yy = b + dy[i]
            if 0 <= xx < r and 0 <= yy < c and visited[xx][yy] == 0 and graph[xx][yy] != '#':  # xx->r 이고 yy->c 인 것 주의!
                queue.append([xx, yy])
                visited[xx][yy] = 1
                if graph[xx][yy] == 'o':
                    oo += 1
                elif graph[xx][yy] == 'v':
                    vv += 1

    # oo와 vv는 지역변수라서 BFS 함수 내에서 비교 실행
    if oo and vv:  # oo와 vv 둘 다 0이 아니여야 비교 실행
        if oo > vv:
            v -= vv
        else:
            o -= oo


r, c = map(int, input().split()) # 마당의 행과 열

graph = [[0]*c for _ in range(r)]
visited = [[0]*c for _ in range(r)]
for i in range(r):
    lst = sys.stdin.readline().rstrip()
    for index, j in enumerate(lst):
        graph[i][index] = j

# 전체 양과 늑대 수 구하기
o = 0
v = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'o':
            o += 1
        elif graph[i][j] == 'v':
            v += 1

# 방향 확인용 좌표 dx, dy
# 좌/우/상/하
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 한 울타리를 만나면(=o나 v를 만나면) BFS 호출
for i in range(r):
    for j in range(c):
        if (graph[i][j] == 'o' or graph[i][j] == 'v') and visited[i][j] == 0:
            BFS(i, j)

print(o, v)