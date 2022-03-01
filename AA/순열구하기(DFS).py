import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 순열 구하기

def DFS(L):  # L은 뽑는 개수
    global cnt
    if L == m:
        for j in range(len(res)):
            print(res[j], end=' ')
        cnt += 1
        print()
    else:
        for i in range(1, n+1):
            if ch[i] != 1:  # 중복 체크
                res[L] = i
                ch[i] = 1
                DFS(L+1)
                ch[i] = 0  # 되돌리기


n, m = map(int, input().split())
res = [0]*m
cnt = 0
ch = [0]*(n+1)
DFS(0)
print(cnt)