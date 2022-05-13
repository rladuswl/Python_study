import sys
sys.stdin = open("input.txt", "rt")
#input = sys.stdin.readline

# 안전영역 (DFS, BFS 풀이)

# 높이가 1부터 100 이하

'''DFS 풀이'''

def dfs(x, y, h):
    visited[i][j] = 1

    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0 <= xx < n and 0 <= yy < n:
            if visited[xx][yy] == 0 and graph[xx][yy] > h:
                dfs(xx, yy, h)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

mmax = -2147000000
for i in range(n):
    for j in range(n):
        if graph[i][j] > mmax:
            mmax = graph[i][j]

cnt = 0
res = 0
for h in range(0, 100):  # 높이가 100 이면 안전영역은 0개이기 때문에 할 필요 X
    if h == mmax:
        break
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] > h:
                cnt += 1
                dfs(i, j, h)

    res = max(res, cnt)
print(res)






'''BFS 풀이
from collections import deque

sys.setrecursionlimit(10**6)

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
for x in range(0, 101, 1):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
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



print(ans)
'''
