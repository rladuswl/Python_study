## 백준 1439 뒤집기
# 그리디

import sys
#input = sys.stdin.readline

s = input()

lst = []
for i in range(1, len(s)):
    if s[i-1] != s[i]:
        lst.append(i)

if (len(lst)%2) == 0:  # 변화되는 부분이 짝수개 이면
    print(len(lst)//2)
elif (len(lst)%2) == 1:
    print((len(lst)//2)+1)
