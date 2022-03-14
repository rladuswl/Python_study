import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 동전 바꿔주기 (DFS)

'''풀이방법 듣고 풀기
def DFS(L, s):
    global cnt
    if s > t:  # 컷 엣지
        return
    if L == k:
        if s == t:
            cnt += 1
    else:
        for i in range(coin[L][1]+1):
            DFS(L+1, s+(i*coin[L][0]))


if __name__ == '__main__':
    t = int(input())  # 지폐의 금액
    k = int(input())  # 동전의 가지 수
    coin = []
    for _ in range(k):
        coin.append(list(map(int, input().split())))
    cnt = 0
    DFS(0, 0)
    print(cnt)
'''
'''강의해설
def DFS(L, sum):
    global cnt
    if sum > t:
        return
    if L == k:
        if sum == t:
            cnt += 1
    else:
        for i in range(0, cn[L]+1):
            DFS(L+1, sum+(i*cv[L]))



if __name__ == '__main__':
    t = int(input())  # 지폐의 금액
    k = int(input())  # 동전의 가지 수
    cv = list()  # 동전 종류(금액)
    cn = list()  # 동전 개수
    for i in range(k):
        a, b = map(int, input().split())
        cv.append(a)
        cn.append(b)
    cnt = 0
    DFS(0, 0)
    print(cnt)
'''

'''DP풀이'''
t=int(input())
n=int(input())
dy=[0]*(t+1)
dy[0]=1
print(dy)
for i in range(n):
    a, b=map(int, input().split())
    for j in range(t, 0, -1):
        for k in range(1, b+1):
            if(j-a*k<0):
                break
            dy[j]+=dy[j-a*k]
            print(dy)
        print('-')
print(dy[t])