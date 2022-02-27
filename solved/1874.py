# 백준 1874 스택수열

import sys
input = sys.stdin.readline

n = int(input())

count = 0
stack = []
result = []
m = True

for _ in range(n):
    x = int(input())

    while count < x:
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        m = False
        break

if m == False:
    print('NO')
else:
    print('\n'.join(result))