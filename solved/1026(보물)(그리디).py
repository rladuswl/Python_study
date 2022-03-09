## 백준 1026 보물

import sys
input = sys.stdin.readline

# A 배열에서 가장 작은 수와 B 배열에서 가장 큰 수를 곱하고, 사용한 것은 pop하는 방식으로 계산


'''min과 max 함수 이용해서 풀기
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0
for _ in range(n):
    a_min = min(a)
    b_max = max(b)
    result += (a_min*b_max)
    a.pop(a.index(a_min))
    b.pop(b.index(b_max))
print(result)
'''

'''a배열 정렬해서 풀기'''
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

result = 0
for i in range(n):
    result += a[i]*b.pop(b.index(max(b)))
print(result)