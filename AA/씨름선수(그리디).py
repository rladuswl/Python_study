import sys
sys.stdin = open("input.txt", "rt")

# 해설 - for 문 하나로 더 효율적 코드 가능

## 씨름선수 (그리디)
'''내 답안
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

li.sort(key = lambda x : (x[1], x[0]), reverse=True)
print(li)

cnt = 0  # 탈락 인원
for i in range(n):
    for j in range(i+1, n):
        if li[i][1] < li[j][1]:
            cnt += 1
            break

print(n-cnt)
'''

'''모범답안'''
n = int(input())
body = []
for i in range(n):
    a, b = map(int, input().split())
    body.append((a, b))

body.sort(reverse=True)
largest = 0
cnt = 0
for x, y in body:
    if y > largest:
        largest = y
        cnt += 1

print(cnt)
