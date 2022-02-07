import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")

# 맞았는데 for문 횟수 줄여보기

## 공주 구하기 (큐)
'''내 답안
n, k = map(int, input().split())

queue = deque()

for i in range(n):
    queue.append(i+1)

while len(queue) != 1:  # 큐 길이가 0이면 거짓
    for i in range(k):
        if i == k-1:
            queue.popleft()
        else:
            queue.append(queue.popleft())

print(queue[0])
'''
'''모범답안'''
n, k = map(int, input().split())

queue = deque()

for i in range(n):
    queue.append(i+1)

while len(queue) != 1:  # 큐 길이가 0이면 거짓
    for i in range(k-1):
        queue.append(queue.popleft())
    queue.popleft()

print(queue[0])