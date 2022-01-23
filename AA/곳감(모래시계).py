import sys
#sys.stdin = open("input.txt", "rt")

# 블로그
# 틀린 문제
# 방식 알아두기
# pop()은 맨 마지막 리턴 후 삭제

## 곳감 (모래시계)
'''내 답안 -------------------- 틀림
n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
mlist = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    if mlist[i][1] == 0:  # 왼쪽
        for j in range(n):
            temp = nlist[mlist[i][0]-1][j]
            a = j-mlist[i][2]
            if a < 0:
                a = a+n
            nlist[mlist[i][0]-1][j] = nlist[mlist[i][0]-1][a]
            nlist[mlist[i][0]-1][a] = temp
    if mlist[i][1] == 1:  # 오른쪽
        for j in range(n):
            temp = nlist[mlist[i][0]-1][j]
            a = j+3
            if a >= n:
                a = a-n
            nlist[mlist[i][0]-1][j] = nlist[mlist[i][0]-1][a]
            nlist[mlist[i][0]-1][a] = temp

print(nlist)
'''

'''해설 듣고 다시 푸는 내 답안 ------- 또 틀림 ㅋ
n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
mlist = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    if mlist[i][1] == 0:
        for j in range(mlist[i][2]):
            temp = nlist[mlist[i][0]-1][0]
            for k in range(1, n):
                nlist[mlist[i][0]-1][k-1] = nlist[mlist[i][0]-1][k]
            nlist[mlist[i][0]-1][n-1] = temp
    elif mlist[i][1] == 1:
        for j in range(mlist[i][2]):
            temp = nlist[mlist[i][0]-1][n-1]
            for k in range(n-1, 0, -1):
                nlist[mlist[i][0]-1][k] = nlist[mlist[i][0]-1][k-1]
            nlist[mlist[i][0]-1][0] = temp

s = 0
e = n-1
sum = 0

for i in range(n):
        for j in range(s, e+1):
            sum += nlist[i][j]
        if s < n//2:
            s += 1
            e -= 1
        else:
            s -= 1
            e += 1

print(sum)
'''

'''모범답안'''
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    h, t, k = map(int, input().split())

    if t == 0:  # 왼쪽
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))  # 0번 인덱스 꺼내서 맨 뒤로 넣기. 나머지 데이터는 빈자리 채우러 앞으로 땡겨지기 때문.
    elif t == 1:  # 오른쪽
        for _ in range(k):
            a[h - 1].insert(0, a[h - 1].pop())

s = 0
e = n-1
sum = 0

for i in range(n):
    for j in range(s, e+1):
        sum += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(sum)