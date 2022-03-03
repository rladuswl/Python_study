import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 조합 구하기

# 1. 중복x, 부분집합
# 2. DFS로 부분집합 구하기, 중복은 check 변수로 제거
'''틀림 21번줄에 s+i가 아니라 i+1임
def DFS(L, s):
    global cnt
    if L == m:
        for x in result:
            print(x, end=' ')
        print()
        cnt += 1
        return
    else:
        for i in range(s, n+1):
            result[L] = i
            DFS(L+1, s+i)


n, m = map(int, input().split())
result = [0]*m
cnt = 0
DFS(0, 1)
print(cnt)
'''

def DFS(L, s):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        cnt += 1
        print()
    else:
        for i in range(s, n+1):
            res[L] = i
            DFS(L+1, i+1)  # 가지에 +1을 해야하므로 i+1


n, m = map(int, input().split())
res = [0]*(n+1)
cnt = 0
DFS(0, 1)
print(cnt)