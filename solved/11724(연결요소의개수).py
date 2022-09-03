import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000)

# 인접행렬 or 인접리스트? -> 인접행렬

def dfs(start):
    visited[start] = 1

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(n+1)
count = 0
for i in range(1, n+1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = 1
        else:
            dfs(i)
            count += 1

print(count)