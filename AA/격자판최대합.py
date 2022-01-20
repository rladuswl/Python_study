import sys
sys.stdin = open("input.txt", "rt")

## 격자판 최대합
'''내 답안
n = int(input())
pan = []
for _ in range(n):
    list1 = list(map(int, input().split()))
    pan.append(list1)

# 행의 합 중에 최대값
max1 = 0
for i in range(n):
    sum1 = 0
    for j in pan[i]:
        sum1 += j
    if sum1 > max1:
        max1 = sum1

# 열의 합 중에 최대값
for i in range(n):
    sum2 = 0
    for j in range(n):
        sum2 += pan[j][i]
    if sum2 > max1:
        max1 = sum2

# 왼->오 대각선
sum3 = 0
for i in range(n):
    sum3 += pan[i][i]
if sum3 > max1:
    max1 = sum3

# 오->왼 대각선
sum4 = 0
for i in range(n):
    sum4 += pan[i][(n-1)-i]
if sum4 > max1:
    max1 = sum4

print(max1)
'''

'''모범답안'''
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

largest = -2147000000  # 가장 작은 값

# 행과 열 최대값
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]  # 행 고정 열 반복
        sum2 += a[j][i]  # 열 고정 행 반복
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

# 대각선
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][(n - 1) - i]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)