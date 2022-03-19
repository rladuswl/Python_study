## 백준 1015 수열 정렬

'''내풀이
## 백준 1015 수열 정렬

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

A_sort = sorted(A)
P = []
for i in range(len(A)):
    idx = A_sort.index(A[i])
    P.append(idx)
    A_sort[idx] = '.'

for x in P:
    print(x, end=' ')
'''

import sys
input = sys.stdin.readline

A_size = int(sys.stdin.readline())
A = sys.stdin.readline().replace("\n", "").split(' ')
A = [int(i) for i in A]

sorted_A = [i for i in A]
sorted_A.sort()

P = []

for i in A:
    P.append(sorted_A.index(i))
    # 이미 할당한 숫자는 sorted_A에서 -1로 대체해 재탐색되지 않도록 함.
    sorted_A[sorted_A.index(i)] = -1

results = [i for i in P]

for result in results:
    sys.stdout.write(str(result) + ' ')

