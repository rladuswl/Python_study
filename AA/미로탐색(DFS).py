import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# 미로탐색 (DFS)

# 상하좌우 방향키 정해서 깊이 탐색하기
# 하나의 노드는 하나의 좌표, 노드에서 뻗는 가지 4개는 상하좌우


def dfs(x, y):
    global cnt

    if x == 6 and y == 6:  # 도착 지점에 오면
        cnt += 1
        return
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if (0 <= xx < 7) and (0 <= yy < 7) and (graph[xx][yy] == 0):
                graph[xx][yy] = 1
                dfs(xx, yy)
                graph[xx][yy] = 0


graph = []
for _ in range(7):
    graph.append(list(map(int, input().split())))
# graph = [list(map(int, input().split())) for _ in range(7)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

cnt = 0  # 방법의 수
graph[0][0] = 1  # graph에다가 방문 체크하기
dfs(0, 0)
print(cnt)

