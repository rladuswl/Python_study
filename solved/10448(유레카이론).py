'''
import sys
input = sys.stdin.readline
from itertools import combinations

def T(n):
    return n*(n+1)//2

t = int(input())

lst = []
for _ in range(t):
    n = int(input())
    i = 1
    while True:
        if T(i) > n:
            break
        lst.append(T(i))
        i += 1
    for combi in combinations(lst, 3):
        if sum(combi) == n:
            print(1)
            break
    else:
        print(0)
'''

import sys
input = sys.stdin.readline

t_lst = [n*(n+1)//2 for n in range(1, 46)]  # 45번째 삼각수 == 1035
eur = [0] * 1001

for i in t_lst:
    for j in t_lst:
        for k in t_lst:
            if i+j+k <= 1000:
                eur[i+j+k] = 1  # i, j, k로 만들어지는 수에 모두 1

t = int(input())
for _ in range(t):
    print(eur[int(input())])

