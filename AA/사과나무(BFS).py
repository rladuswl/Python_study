import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

from collections import deque

# 최상단 노드는 n*n 격자판의 정중앙 좌표 값!

'''bfs 방식으로 풀기'''
def bfs(x, y):
    global s
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    s += lst[x][y]

    L = 0
    while True:
        if L==n//2:
            break
        size = len(q)  # pop 하기 전에 size 구하기
        # print("size", size)
        for i in range(size):
            tmp = q.popleft()
            for j in range(4):
                x = tmp[0] + dx[j]
                y = tmp[1] + dy[j]
                if visited[x][y] == 0:
                    visited[x][y] = 1
                    q.append((x, y))
                    s += lst[x][y]
        # print(L, tmp)
        # for i in range(len(visited)):
        #     print(visited[i])
        L += 1


n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
s = 0
bfs(n//2, n//2)
print(s)