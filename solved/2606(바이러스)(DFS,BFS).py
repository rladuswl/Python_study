import sys
input = sys.stdin.readline

## 백준 2606 바이러스
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

# 상위 노드와 하위 노드가 명확히 정해진 것이 아니기 때문에
# 트리 방식 보다는 그래프 방식으로 생각하여 풀기

## DFS 방식
# 바이러스가 걸린 경로들을 visited에 저장한 후 최종 출력에서 본인 1을 제외한 나머지 노드 개수 출력
'''
graph = {}

n = int(input())
m = int(input())

for i in range(n):
    graph[i+1] = set()  # 1~n

for j in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

def DFS(start, graph):
    for i in graph[start]:
        if i not in visited:
            visited.append(i)
            DFS(i, graph)

visited = []
DFS(1, graph)
print(len(visited) - 1)
'''

## BFS 방식
# 큐 방식 사용 (데큐가 아니라 리스트랑 다름없..)

graph = {}

n = int(input())
m = int(input())

for i in range(n):
    graph[i+1] = set()  # 1~n

for j in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
#print(graph)

def BFS(start, graph):
    queue = [start]
    while queue:
        for i in graph[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                #print(queue)

visited = []
BFS(1, graph)
print(len(visited) - 1)
#print(visited)