import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

## 응급실
'''내 답안
n, m = map(int, input().split())
queue = list(map(int, input().split()))
queue = deque(queue)
cnt = 0

while 1:
    a = queue.popleft()
    print(a)

    for i in range(len(queue)):
        if queue[i] > a:
            queue.append(a)
            break
    else:
        cnt += 1
        if i == m:
            print(cnt)
            break
'''

'''모범답안'''
n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0
while True:
    cur = Q.popleft()
    if any(cur[1]<x[1] for x in Q):  # 뒤에 위험도가 높은 사람이 한 명이라도 있으면 true
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            break
print(cnt)