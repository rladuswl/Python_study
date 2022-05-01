import sys
# sys.stdin = open("input.txt", "rt")
# input = sys.stdin.readline

# 섬나라 아일랜드 (BFS)

from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    graph[i][j] = 0

    while q:
        x, y = q.popleft()
        for a in range(8):
            xx = x + dx[a]
            yy = y + dy[a]
            if (0 <= xx < n) and (0 <= yy < n):
                if graph[xx][yy] == 1:
                    graph[xx][yy] = 0
                    q.append((xx, yy))


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)
            cnt += 1

print(cnt)
