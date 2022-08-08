import sys
input = sys.stdin.readline

n = int(input())

tmp = 0

for _ in range(n):
    s = input().rstrip()
    lst = []
    for i in range(len(s)):
        if s[i] not in lst:
            lst.append(s[i])
        elif s[i] in lst and s[i] == s[i-1]:
            continue
        else:
            break
    else:
        tmp += 1

print(tmp)