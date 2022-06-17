import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# 사다리 타기(DFS)
# 0~9까지 모든 열을 보는 것은 비효율적
# 9번 행을 보고 2를 찾아서 역으로 사다리를 타고 올라가기
# 9번 행부터 0번 행까지 오른쪽, 왼쪽을 살피며 올라가고
# 0번 행이 되었을 때의 열 값을 출력하면 됨


def dfs(x, y):
    visited[x][y]=1
    if x == 0:
        print(y)
    else:
        if y-1>=0 and graph[x][y-1] == 1 and visited[x][y-1]==0:
            dfs(x, y-1)
        elif y+1<10 and graph[x][y+1] == 1 and visited[x][y+1]==0:
            dfs(x, y+1)
        else:
            dfs(x-1, y)

graph = [list(map(int, input().split())) for _ in range(10)]
visited = [[0]*10 for _ in range(10)]

for y in range(10):
    if graph[9][y] == 2:
        dfs(9, y)
