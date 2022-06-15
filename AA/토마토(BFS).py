import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# 토마토 (BFS 활용)
# 1. 모든 토마토가 익어있는 상태인지 확인
# 2. 이중 for문으로 한 칸씩 접근하면서 1이면 bfs 호출하고 그 주변의 안 익은 토마토(0)를 익은 상태(1)로 바꾸기
# 3. 만약 익은 토마토가 하나도 없다면 -1 출력

n, m = int(input().split())
graph = [[]*n for _ in range(m)]

print(graph)