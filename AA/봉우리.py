import sys

sys.stdin = open("input.txt", "rt")

# 해설방식 참고하면 좋음

## 봉우리
'''내 답안
n = int(input())
# 먼저 (n+1 * n+1) 리스트를 전부 0으로 초기화 한다.
tot = [[0 for _ in range(n+2)] for _ in range(n+2)]

for i in range(1, n+1):
    list1 = list(map(int, input().split()))
    for j in range(0, n):
        tot[i][j+1] = list1[j]

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if max(tot[i-1][j], tot[i+1][j], tot[i][j-1], tot[i][j+1]) < tot[i][j]:
            cnt += 1

print(cnt)
'''

'''모범답안'''
dx = [-1, 0, 1, 0]  # 상하좌우 풀 때 dx, dy 리스트 초기화 하여 푸는 방법
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)

for x in a:  # 각 행마다 맨 앞과 맨 뒤에 0 넣기
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):  # all은 모두 참일 때 True
            cnt+=1

print(cnt)