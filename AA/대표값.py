import sys
sys.stdin = open("input.txt", "rt")

## 대표값
'''내 답안
n = int(input())
list1 = list(map(int, input().split()))

sum = 0
aver = 0
for i in list1:
    sum += i
aver = int(round(sum/n, 0))  # 소수 첫째 자리에서 반올림

# 평균과 점수의 차이가 최소여야 함
min = float('inf')
for i in range(len(list1)):
    if abs(aver-list1[i]) < min:
        min = abs(aver-list1[i])

max = 0
for j in range(len(list1)):
    if abs(aver-list1[j]) == min:
        if max < list1[j]:
            max = list1[j]
            a = j+1

print(aver, a)
'''

# round는 round_half_even 방식 -> 정확히 half 지점에 있을 때 짝수를 근사값으로 택함
'''해답
n = int(input())
a = list(map(int, input().split()))
# ave = round(sum(a)/n)
ave = sum(a)/n
ave = ave + 0.5
ave = int(ave)
min = 2147000000  # 정수형에서 가장 큰 수
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx+1
    elif tmp == min:
        if x > score:
            score = x
            res = idx+1

print(ave, res)
'''