## import itertools as it

'''라이브러리를 사용한 순열
import sys
import itertools as it
sys.stdin = open("input.txt", "rt")

n, f = map(int, input().split())
b = [1]*n

for i in range(1, n):
    b[i] = (b[i-1]*(n-i))//i
a = list(range(1, n+1))

for tmp in it.permutations(a):
    sum = 0
    for L, x in enumerate(tmp):
        sum += (x*b[L])
    if sum == f:
        for x in tmp:
            print(x, end=' ')
        break
'''

'''라이브러리를 사용한 조합'''

import sys
import itertools as it
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())

cnt = 0
for x in it.combinations(a, k):  # a라는 리스트에서 k개 뽑기
    if sum(x) % m == 0:
        cnt += 1

print(cnt)
