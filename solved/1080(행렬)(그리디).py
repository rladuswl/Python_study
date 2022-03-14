## 백준 1080 행렬
# 그리디

import sys
#input = sys.stdin.readline

def reverse(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            A[x][y] = 1 - A[x][y]

n, m = map(int, input().split())  # 행 열

#A = [list(map(int, list(input()))) for _ in range(n)]
A = []
for i in range(n):
    A.append(list(map(int, input())))
B = [list(map(int, list(input()))) for _ in range(n)]

cnt = 0
for i in range(0, n-2):  # 수행범위 : 0
    for j in range(0, m-2):  # 수행범위 : 0, 1
        if A[i][j] != B[i][j]:
            reverse(i, j)  # 변환 함수
            cnt += 1  # 변환 횟수 +1

# 변환 끝낸 후 일치하는지 확인
isSame = True
for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            isSame = False
            break

if isSame == False:
    print(-1)
else:
    print(cnt)