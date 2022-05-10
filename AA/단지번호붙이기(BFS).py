import sys
sys.stdin = open("input.txt", "rt")
#input = sys.stdin.readline

# 단지 번호 붙이기 (DFS, BFS)

## BFS로 풀기
from collections import deque


def bfs(i, j, a):
    global cnt
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    cnt += 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if (0 <= xx < n) and (0 <= yy < n):
                if (visited[xx][yy] == 0) and (graph[xx][yy] == 1):
                    graph[xx][yy] = a
                    q.append((xx, yy))
                    cnt += 1


n = int(input())
graph = []
#graph = [list(map(int, input())) for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

cnt = 0
a = 2
answer = []
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j, a)
            a += 1
            answer.append(cnt)
            cnt = 0

print(len(answer))
answer.sort()
for x in answer:
    print(x)