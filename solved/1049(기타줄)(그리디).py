## 백준 1049 기타줄

'''틀림
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 끊어진 줄의 개수 n과 브랜드 m개

p_sum = 2147000000
sum = 2147000000
last = 0
how_p = 0
for _ in range(m):

    a, b = map(int, input().split())  # 패키지 가격 a와 낱개 가격 b

    if n > 6:
        last = n%6  # 6개짜리 패키지 사고 남은 더 사야할 줄 개수
        how_p = n//6  # 패키지 몇 개 사는지
        if how_p*a < p_sum:
            p_sum = (how_p*a)
        #if last*b < sum:
            sum = (last*b)
    else:
        if n*b < sum:
            sum = (n*b)

    if p_sum+sum > ((how_p+1)*a):
        p_sum = (how_p+1)*a
        sum = 0

print(p_sum+sum)
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 끊어진 줄의 개수 n과 브랜드 m개

pack_list = []
one_list = []
for _ in range(m):
    a, b = map(int, input().split())  # 패키지 가격 a와 낱개 가격 b
    pack_list.append(a)
    one_list.append(b)

pack_list.sort()  # 인덱스 0이 패키지 가격이 가장 싸다.
one_list.sort()  # 인덱스 0이 낱개 가격이 가장 싸다.

result = 0
if pack_list[0] <= one_list[0]*6:
    p = n//6
    last = n%6
    result = (p*pack_list[0]) + (last*one_list[0])
    if ((p+1)*pack_list[0]) < result:
        result = (p+1)*pack_list[0]
else:
    result = one_list[0]*n

print(result)