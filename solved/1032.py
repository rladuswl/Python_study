# 명령 프롬프트 1032
# 구현, 문자열

import sys
input = sys.stdin.readline

n = int(input())

res = []  # 입력값과 비교하는 값
for i in range(n):
    s = list(sys.stdin.readline().rstrip())

    if i == 0:
        res = s
    else:
        for j in range(len(s)):
            if s[j] != res[j]:
                res[j] = '?'

for x in res:
    print(x, end='')