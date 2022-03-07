import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 경로 탐색 (그래프 DFS)
'''
def DFS(start):
    global cnt

    visited[start] = 1

    if start == n:
        cnt += 1
    else:
        for i in graph[start]:
            if visited[i] == 0:
                visited[i] = 1
                DFS(i)
                visited[i] = 0
    return cnt

if __name__ == '__main__':
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    cnt = 0
    visited = [0]*(n+1)
    print(DFS(1))
'''

def DFS(v):
    global cnt
    global res

    if v == n:
        cnt += 1
        for x in res:
            print(x, end=' ')
        print()

    else:
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited[i] == 0:
                res.append(i)
                visited[i] = 1
                DFS(i)
                visited[i] = 0
                res.pop()

if __name__ == '__main__':
    n, m = map(int, input().split())

    graph = [[0]*(n+1) for _ in range(n+1)]
    visited = [0]*(n+1)
    for i in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
    cnt = 0
    visited[1] = 1
    res = []
    res.append(1)
    DFS(1)
    print(cnt)
