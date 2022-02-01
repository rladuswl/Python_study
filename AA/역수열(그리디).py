import sys
sys.stdin = open("input.txt", "rt")

# 틀림, 다시푼거 맞음
# 1~n 으로 정렬한 숫자를 처리하기

## 역수열 (그리디)
'''내 답안
n = int(input())
li = list(map(int, input().split()))

tmp = [n for _ in range(n)]

for i in range(n):
    cnt = 0
    seat = 0
    if li[i] != 0:
        for j in range(n):
            if tmp[j] > i+1:
                cnt += 1
                seat += 1
            else:
                seat += 1
            if cnt == li[i]:
                break

    while tmp[seat] != 8:
        seat += 1
    tmp[seat] = i+1

for x in tmp:
    print(x, end=' ')
'''

'''다시 풀기
n = int(input())
li = list(map(int, input().split()))

tmp = [0 for _ in range(n)]

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == li[i]:
            break
        if tmp[j] == 0:
            cnt += 1
    while tmp[j] != 0:
        j+=1
    tmp[j] = i+1

for x in tmp:
    print(x, end=' ')
'''

'''모범답안'''
n = int(input())
a = list(map(int, input().split()))
seq = [0]*n

for i in range(n):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:  # 앞에 빈공간 확보 and 자리가 생기면
            seq[j] = i+1
            break
        elif seq[j] == 0:
            a[i] -= 1
for x in seq:
    print(x, end=' ')