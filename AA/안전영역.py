import sys
sys.stdin = open("input.txt", "rt")
#input = sys.stdin.readline

# 안전영역

# 높이가 1부터 100 이하
from collections import deque

def bfs(a, i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if (0<=xx<n) and (0<=yy<n) and (visited[xx][yy]==0):
                if graph[xx][yy] > a:
                    q.append((xx, yy))
                    visited[xx][yy]=1


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

mmax = -2147000000
mmin = 2147000000
for i in range(n):
    for j in range(n):
        if graph[i][j] > mmax:
            mmax = graph[i][j]
        if graph[i][j] < mmin:
            mmin = graph[i][j]

ans = -2147000000 # 안전한 영역의 최대 개수
cnt = 0
for x in range(1, 101, 1):
    visited = [[0] * n for _ in range(n)]
    if x < mmin:
        result = 1
        if result > ans:
            ans = result
        continue
    elif x > mmax:
        result = 0
        if result > ans:
            ans = result
        continue
    for i in range(n):
        for j in range(n):
            if graph[i][j] > x and visited[i][j]==0:
                bfs(x, i, j)
                cnt += 1
    if cnt > ans:
        ans = cnt
        cnt = 0
    print()
    for q in range(n):
        for p in range(n):
            print(visited[q][p], end='')
        print()

print("답", ans)