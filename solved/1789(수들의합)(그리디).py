## 백준 1789 수들의 합
# 그리디, 수학

'''답안
import sys
input = sys.stdin.readline

s = int(input())

result = 0
count = 0
while True:
    count += 1
    result += count
    if result > s:
        break
print(result)
print(count-1)
'''

import sys
input = sys.stdin.readline

s = int(input())

result = 0
i = 1
while (result+i) <= s:
    result += i
    i += 1

print(i-1)
