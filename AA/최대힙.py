import sys
sys.stdin = open("input.txt", "rt")

## 최대힙
# 부모 노드가 자식 노드보다 항상 커야 한다.
# 따라서 root 노드가 가장 크다.

# heapq의 기본이 최소값인 것을 이용해서 부호를 바꿔서 push 한다.
'''
import heapq

h = []
while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        if len(h) == 0:
            print(-1)
        else:
            a, b = heapq.heappop(h)
            print(b)
    elif n == -1:
        break
    else:
        heapq.heappush(h, (-n, n))
'''

''' 조금 더 간단하게 변형'''
import heapq

h = []
while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        if len(h) == 0:
            print(-1)
        else:
            print(-heapq.heappop(h))
    elif n == -1:
        break
    else:
        heapq.heappush(h, -n)