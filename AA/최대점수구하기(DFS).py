import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 섹션 7. 최대점수 구하기(DFS)

# 1. 푸는데 걸리는 시간들 중 부분집합이 m이 되어야 한다.
# 2. 부분집합을 구하는 DFS
'''틀림
def DFS(L, time, sum):
    global res

    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                DFS(i, time+graph[i][1], sum+graph[i][0])
                visited[i] = 0
                DFS(i, time, sum)



if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        a, b = map(int, input().split())
        graph.append([a, b])
    visited = [0]*n
    res = 0  # 최대 점수
    DFS(0, 0, 0)
    print(res)
'''


'''강의 정답(부분집합)'''
def DFS(L, time, sum):
    global res

    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
            print(L, time, sum)
    else:
        print(L, time, sum)
        DFS(L+1, time+graph[L][1], sum+graph[L][0])
        DFS(L+1, time, sum)


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        a, b = map(int, input().split())
        graph.append([a, b])
    res = 0  # 최대 점수
    DFS(0, 0, 0)
    print(res)


'''조합으로 구하기

def DFS(s, time, sum):
    global max
    if time > m:
        return
    if sum > max:
        max = sum
    for i in range(s, n):
        print(s, i, time, sum)
        DFS(i+1, time+graph[i][1], sum+graph[i][0])



if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        a, b = map(int, input().split())
        graph.append([a, b])
    max = -2147000000
    DFS(0, 0, 0)
    print(max)
'''