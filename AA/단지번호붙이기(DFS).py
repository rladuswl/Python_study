import sys
sys.stdin = open("input.txt", "rt")
#input = sys.stdin.readline

# 단지 번호 붙이기 (DFS, BFS)

## DFS로 풀기

def dfs(i, j):
    global cnt

    graph[i][j] = 0

    for a in range(4):
        xx = i + dx[a]
        yy = j + dy[a]
        if (0<=xx<n) and (0<=yy<n):
            if graph[xx][yy] == 1:
                dfs(xx, yy)
                cnt += 1


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

cnt_array = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 1
            dfs(i, j)
            cnt_array.append(cnt)

print(len(cnt_array))
cnt_array.sort()
for x in cnt_array:
    print(x)