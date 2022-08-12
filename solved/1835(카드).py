import sys
input = sys.stdin.readline

n = int(input())

from collections import deque
q = deque()

q.append(n)

for i in range(n-1, 0, -1):
    q.appendleft(i)
    for _ in range(i):
        q.appendleft(q.pop())
print(*q)
