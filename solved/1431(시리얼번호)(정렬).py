## 백준 1431 시리얼 번호

import sys
#input = sys.stdin.readline


# 숫자들의 합
def num_sum(x):
    s = 0
    for i in x:
        if i.isdecimal():
            s += int(i)
    return s


n = int(input())

lst = list()
for _ in range(n):
    lst.append(input())

lst.sort(key = lambda x : (len(x), num_sum(x), x))  # 차례대로 x길이, 숫자들의 합, 사전순

for x in lst:
    print(x, end=' ')