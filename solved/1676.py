# 백준 1676 팩토리얼 0의 개수

import sys

n = int(sys.stdin.readline())

result = 1
for i in range(1, n+1):
    result *= i

result_list = list(str(result))
result_list.reverse()

cnt = 0
for x in result_list:
    if x != '0':
        print(cnt)
        break
    else:
        cnt += 1