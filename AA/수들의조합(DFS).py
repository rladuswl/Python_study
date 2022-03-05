import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 수들의 조합

# = 3개짜리 부분집합 만들기와 같음

# 1. DFS + 조합구하기
# 2. if에서 sum이 n의 배수이면 cnt에 +1 하기

def DFS(L, s):  # L은 0~k까지, s는 lst 안의 값들의 인덱스 시작점
    global cnt

    if L == k:
        sum = 0
        #print(res)
        for x in res:
            sum += x
        if sum%m == 0:
            cnt += 1

    else:
        for i in range(s, n):
            res[L] = lst[i]
            DFS(L+1, i+1)  # s+1에서 i+1로 바꿔보았더니니 성공.. 이유는?




if __name__ == '__main__':
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    res = [0]*k
    DFS(0, 0)
    print(cnt)