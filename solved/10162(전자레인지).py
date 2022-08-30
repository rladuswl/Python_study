import sys
input = sys.stdin.readline

# 첫 번째 방법
'''
m = int(input())

a = 300
b = 60
c = 10

if m%10 != 0:
    print(-1)
    sys.exit(0)

if m//a > 0:
    mm = m%a
    print(m//a, end=' ')
else:
    mm = m
    print(0, end=' ')

if mm//b > 0:
    mmm = mm%b
    print(mm//b, end=' ')
else:
    mmm = mm
    print(0, end=' ')

if mmm//c > 0:
    print(mmm//c, end=' ')
else:
    print(0, end=' ')
'''

# 두 번째 방법
m = int(input())

count = [0] * 3  # 300, 60, 10의 각각 카운트
abc = [300, 60, 10]

if (m%10 != 0):
    print(-1)
else:
    for i in range(3):
        count[i] = m//abc[i]
        m = m%abc[i]

    print(count[0], count[1], count[2])