import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 휴가 (삼성 SW역량평가 기출문제 : DFS 활용)

# 조합인데 조건이 추가됨
'''조합'''
def DFS(s, money):
    global max

    if s > (n+1):
        return
    if s == (n+1):
        if money > max:
            max = money

    for i in range(s, n+1):
        if i+graph[i][0] <= (n+1):
            DFS(i+graph[i][0], money+graph[i][1])
        DFS(i+1, money)

n = int(input())
graph = []
for _ in range(n):
    a, b = map(int, input().split())
    graph.append([a, b])

graph.insert(0, [0, 0])
max = -2147000000
DFS(1, 0)
print(max)



'''부분집합
def DFS(L, sum):
    global max

    if L == (n+1):
        if sum > max:
            max = sum
    else:
        if L+T[L] <= (n+1):
            DFS(L+T[L], sum+P[L])  # 상담을 했을 때
        DFS(L+1, sum)  # 1씩 증가하다보면 n+1로 가게 됨

n = int(input())
T = list()
P = list()
for _ in range(n):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

max = -2147000000
T.insert(0, 0)  # 인덱스 번호를 1일부터 맞추기 위해 한 칸씩 미루기
P.insert(0, 0)  # 인덱스 번호를 1일부터 맞추기 위해 한 칸씩 미루기
DFS(1, 0)  # 날짜, 돈 합
print(max)
'''