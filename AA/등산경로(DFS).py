import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# 등산경로(DFS)

def dfs(s):
    global cnt
    if s == f:
        cnt += 1
    else:
        for i in range(4):
            xx = s[0] + dx[i]
            yy = s[1] + dy[i]
            if (0 <= xx < n) and (0 <= yy < n) and (graph[s[0]][s[1]] < graph[xx][yy]) and (visited[xx][yy] == 0):
                ss = (xx, yy)
                visited[xx][yy]=1
                dfs(ss)
                visited[xx][yy]=0


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

start = 9999
s = (0, 0)
finish = 0
f = (0, 0)
for i in range(n):
    for j in range(n):
        if start > graph[i][j]:
            start = graph[i][j]
            s = (i, j)
        if finish < graph[i][j]:
            finish = graph[i][j]
            f = (i, j)

visited=[[0]*n for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 0
visited[s[0]][s[1]] = 1
dfs(s)
print(cnt)
