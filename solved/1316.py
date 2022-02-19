# 백준 1316 그룹 단어 체커
# 1. 단어의 인덱스 하나씩 접근하기
# 2. 연속으로 접근하는 경우 제외하고, 리스트에 이미 있으면 그룹 단어 아님
# 3. 없으면 리스트에 추가하기
import sys
n = int(sys.stdin.readline())

cnt = 0
for _ in range(n):
    lst = []

    s = sys.stdin.readline().rstrip()

    for i in range(len(s)):
        if s[i] not in lst:
            lst.append(s[i])
        elif s[i] in lst and s[i] == s[i-1]:
            continue
        else:
            break
    else:
        cnt += 1

print(cnt)