import sys
#sys.stdin = open("input.txt", "rt")

## 최소힙

import heapq

h = []

while 1:
    n = int(sys.stdin.readline().rstrip())
    if n == -1:
        break
    elif n == 0:
        if len(h) == 0:
            print(-1)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, n)